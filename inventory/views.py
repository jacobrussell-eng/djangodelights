from django.shortcuts import render, redirect
from django.db.models import Sum

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientForm, MenuItemForm, RecipeForm, PurchaseForm

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

class IngredientUpdate(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = "inventory/update_ingredient.html"
    form_class = IngredientForm

class IngredientDelete(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "inventory/delete_ingredient.html"
    success_url = reverse_lazy('ingredients')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredient_name"] = self.object.name
        return context

class MenuList(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "inventory/menu_list.html"

class ItemCreate(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = "inventory/add_menu_item.html"
    form_class = MenuItemForm

class PurchaseList(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/purchase_list.html"

class PurchaseCreate(LoginRequiredMixin, CreateView):
    model = Purchase
    template_name = "inventory/add_purchase.html"
    form_class = PurchaseForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_items"] = MenuItem.objects.all()
        return context

    def post(self, request):
        menu_item_id = request.POST["ordered_item"]
        menu_item = MenuItem.objects.get(pk=menu_item_id)
        reqs = menu_item.reciperequirement_set
        purchase = Purchase(ordered_item=menu_item)

        for req in reqs.all():
            req_ing = req.ingredient
            req_ing.quantity -= req.how_many
            req_ing.save()
        
        purchase.save()
        return redirect("/purchases")

class RecipeCreate(LoginRequiredMixin, CreateView):
    template_name = "inventory/add_requirement.html"
    model = RecipeRequirement
    form_class = RecipeForm

class ReportView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/reports.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["purchases"] = Purchase.objects.all()
        revenue = Purchase.objects.aggregate(revenue = Sum("ordered_item__item_price"))["revenue"]
        total_cost = 0
        for purchase in Purchase.objects.all():
            for req in purchase.ordered_item.reciperequirement_set.all():
                total_cost += req.ingredient.unit_price * req.how_many

        context["revenue"] = revenue
        context["total_cost"] = total_cost
        context["profit"] = revenue - total_cost
        return context