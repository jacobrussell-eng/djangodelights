from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientForm, MenuItemForm, RecipeForm

# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredient.objects.all()
        context["menu_items"] = MenuItem.objects.all()
        context["purchases"] = Purchase.objects.all()
        return context
    
def log_out(request):
    logout(request)
    return redirect("/")

class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "inventory/ingredient_list.html"

class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = "inventory/add_ingredient.html"
    form_class = IngredientForm

class MenuList(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "inventory/menu_list.html"

class ItemCreate(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = "inventory/add_item.html"
    form_class = MenuItemForm

class PurchaseList(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/purchase_list.html"

# class PurchaseCreate(LoginRequiredMixin, CreateView):
#     model = Purchase
#     template_name = "inventory/add_purchase.html"
#     form_class = PurchaseForm

class RecipeCreate(LoginRequiredMixin, CreateView):
    template_name = "inventory/add_recipe_requirement.html"
    model = RecipeRequirement
    form_class = RecipeForm

class ReportView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/reports.html"