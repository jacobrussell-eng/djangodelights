from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=6)
    unit_price = models.FloatField(max_length=6)
    def get_absolute_url(self):
        return "/ingredients"
    
    def __str__(self):
        return f"""
        name={self.name};
        qty={self.quantity};
        unit={self.unit};
        unit_price={self.unit_price}
        """

class MenuItem(models.Model):
    item_name = models.CharField(max_length=30)
    item_price = models.FloatField(max_length=6)
    def get_absolute_url(self):
        return "/menu"
    
    def available(self):
        return all(X.enough() for X in self.reciperequirement_set.all())

    def __str__(self):
        return f"title={self.item_name}; price={self.item_price}"

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    how_many = models.FloatField(max_length=6)
    def __str__(self):
        return f"menu_item=[{self.menu_item.__str__()}]; ingredient={self.ingredient.name}; qty={self.how_many}"
    
    def get_absolute_url(self):
        return "/menu"

    def enough(self):
        return self.how_many <= self.ingredient.quantity

class Purchase(models.Model):
    ordered_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    order_time = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"menu_item=[{self.ordered_item.__str__()}]; time={self.order_time}"

    def get_absolute_url(self):
        return "/purchases"