
from django.shortcuts import render, redirect
from .models import Tea, Tea_Type, Ingredients, Photo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
# from .models import Cat, Toy, Photo
from .forms import DrinkForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'TeaCollector'


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid credentials - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class TeaCreate(CreateView):
    model = Tea
    fields = ["name", "origin", "description"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TeaUpdate(UpdateView):
    model = Tea
    fields = ['name', "tea_type", 'origin', 'ingredients']


class TeaDelete(DeleteView):
    model = Tea
    success_url = '/'


def home(request):
    teas = Tea.objects.all()
    return render(request, "home.html", {
        "title": "Home",
        "teas": teas,
    })


def about(request):
    return render(request, "about.html", {
        "title": "About",
    })


@login_required
def teas(request):
    teas = Tea.objects.filter(user=request.user)
    return render(request, "teas/index.html", {
        "teas": teas
    })


@login_required
def tea(request, pk):
    tea = Tea.objects.get(id=pk)
    # tea_type_not = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))
    missing_ingredients = Ingredients.objects.exclude(id__in=tea.ingredients.all().values_list("id"))
    drink_form = DrinkForm()

    return render(request, "teas/detail.html", {
        "title": tea.name,
        "tea": tea,
        "drink_form": drink_form,
        "ingredients": missing_ingredients

    })


@login_required
def add_drink(request, pk):
    # create the ModelForm using the data in request.POST
    form = DrinkForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_drink = form.save(commit=False)
        new_drink.tea_id = pk
        new_drink.save()
    return redirect('detail', pk=pk)


@login_required
def add_photo(request, pk):
    # photo-file was the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, cat_id=cat_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', pk=pk)


def add(request):
    if request.method == "GET":
        return render(request, "add_tea.html", {
            "title": "Add Tea",
        })
    elif request.method == "POST":
        print(", ".join(request.POST.getlist("tea_type")))
        tea = Tea.objects.create(
            name=request.POST["name"],
            origin=request.POST["origin"],
            tea_type=", ".join(request.POST.getlist("tea_type")),
            ingredients=request.POST["ingredients"].title(),
        )
        return redirect("/tea/%s" % tea.id)


def edit(request, pk):
    tea = Tea.objects.get(id=pk)
    if request.method == "GET":
        return render(request, "edit_tea.html", {
            "title": "Edit Tea",
            "tea": tea,
            "tea_types": tea.tea_type.split(", "),
            "ingredients": tea.ingredients.split(", ")
        })
    elif request.method == "POST":
        name = request.POST["name"]
        tea.name = name
        tea.origin = request.POST["origin"]
        tea_type = ", ".join(request.POST.getlist("tea_type"))
        tea.tea_type = tea_type
        tea.ingredients = request.POST["ingredients"].title()
        tea.save()
        return redirect("/tea/%s" % tea.id)


def delete(request, pk):
    Tea.objects.get(id=pk).delete()
    return redirect("/")
