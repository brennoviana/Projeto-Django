from django.shortcuts import render

from recipes.models import Recipe


def home(request):
    recipes = Recipe.objects.all().order_by("-id")
    return render(request, "recipes/pages/home.html", context={
        "recipes": recipes
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id).order_by('-id')
    return render(request, "recipes/pages/home.html", context={
        "recipes": recipes
    })


def recipe(request, recipe_slug):
    recipe = Recipe.objects.filter(slug=recipe_slug)
    return render(request, "recipes/pages/recipe-view.html", context={
        "detail_page": True,
        "recipes": recipe
    })
