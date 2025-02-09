from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', views.log_out, name="logout"),
    path('ingredients/', views.IngredientList.as_view(), name="ingredients"),
    path('menu/', views.MenuList.as_view(), name="menu"),
    path('purchases/', views.PurchaseList.as_view(), name="purchases"),
    path('reports/', views.ReportView.as_view(), name="reports"),
]