# <appname>/urls.py
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.recipe_list, name="recipe_list"),
    path("<int:pk>/", views.recipe_detail, name="recipe_detail"),
]

# This might be needed, depending on your Django version
app_name = "ledger"

