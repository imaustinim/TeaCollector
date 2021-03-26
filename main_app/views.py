from django.shortcuts import render

tea_types = ["black", "green", "herbal", "matcha", "mate", "oolong", "roibos", "white"]


def home(request):
    return render(request, "home.html", {
        "teas": tea_types,
    })
