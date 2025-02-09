from django.contrib import admin
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(RecipeRequirement)
admin.site.register(Purchase)

# Alternatively: [admin.site.register(X) for X in [RecipeRequirement, MenuItem, Ingredient, Purchase]]
