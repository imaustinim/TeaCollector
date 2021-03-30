from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tea


class TeaCreate(CreateView):
    model = Tea
    fields = '__all__'


class TeaUpdate(UpdateView):
    model = Tea

    fields = ['name', "tea_type", 'origin', 'ingredients']


class TeatDelete(DeleteView):
    model = Tea
    success_url = '/'


def home(request):
    teas = Tea.objects.all()
    return render(request, "home.html", {
        "title": "Home",
        "teas": teas,
    })


def tea(request, tea_id):
    tea = Tea.objects.get(id=tea_id)
    return render(request, "tea.html", {
        "title": "Tea",
        "tea": tea,
        "tea_types": tea.tea_type.split(", "),
        "ingredients": tea.ingredients.split(", ")
    })


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


def edit(request, tea_id):
    tea = Tea.objects.get(id=tea_id)
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


def delete(request, tea_id):
    Tea.objects.get(id=tea_id).delete()
    return redirect("/")
