from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

def bio_length_error(value):
    if len(value) < 255:
        raise ValidationError(
            _("Bio length is too short. It must be at least 255 characters."),
        )
    
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(validators=[bio_length_error])
    
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("ledger:ingredient_detail", kwargs={"pk": self.pk})

class Recipe(models.Model):
    
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="recipes")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name    
    def get_absolute_url(self):
        return reverse("ledger:recipe_detail", kwargs={"pk": self.pk})
    
    
class RecipeIngredient(models.Model):    
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name = "ingredients")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name = "recipe")
    quantity = models.CharField(max_length = 100)
    
    def __str__(self):
        return f"{self.recipe.name}: {self.quantity} {self.ingredient.name}"
    