from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', views.log_out, name="logout"),
    path('ingredients/', views.IngredientList.as_view(), name="ingredients"),
    path('ingredients/new', views.IngredientCreate.as_view(), name="add_ingredient"),
    path('ingredients/<slug:pk>/update/', views.IngredientUpdate.as_view(), name="update_ingredient"),
    path('ingredients/<slug:pk>/delete/', views.IngredientDelete.as_view(), name="delete_ingredient"),
    path('menu/', views.MenuList.as_view(), name="menu"),
    path('menu/new', views.ItemCreate.as_view(), name="add_menu_item"),
    path('menu/requirement/', views.RecipeCreate.as_view(), name="add_requirement"),
    path('purchases/', views.PurchaseList.as_view(), name="purchases"),
    path('purchases/new/', views.PurchaseCreate.as_view(), name="add_purchase"),
    path('reports/', views.ReportView.as_view(), name="reports"),
]