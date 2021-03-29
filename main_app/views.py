from django.shortcuts import render

tea_types = ["black", "green", "herbal", "matcha", "mate", "oolong", "roibos", "white"]


def home(request):
    return render(request, "home.html", {
        "teas": tea_types,
    })


def tea(request, tea_id):
    return render(request, "tea.html", {
        "title": tea_types[0],
    })


def add_tea(request):
    return render(request, "add_tea.html", {
        "title": request,
    })


def tea_submit(request):
    print(request)
