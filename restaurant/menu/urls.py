from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('menu/', views.menu, name="menu"),
    path('cart/', views.cart, name="cart"),
]
