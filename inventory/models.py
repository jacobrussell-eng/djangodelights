from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=6)
    unit_price = models.FloatField(max_length=6)

class MenuItem(models.Model):
    item_name = models.CharField(max_length=30)
    item_price = models.FloatField(max_length=6)

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    how_many = models.FloatField(max_length=6)

class Purchase(models.Model):
    ordered_item = models.ForeignKey(MenuItem, on_delete=models.DO_NOTHING) # or CASCADE?
    order_time = models.DateField()
