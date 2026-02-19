# Create your views here.
from django.shortcuts import get_object_or_404, render
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'ledger/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'ledger/recipe.html', {'recipe': recipe})
