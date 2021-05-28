from django.contrib import admin
from django.urls import path
from dz1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.get_all_products),
    path('products/<int:id>/', views.get_one_product),
    path('products/', views.get_all_products),
    path('add_product/', views.add_product),
    path('add_category/', views.add_category),
    path('add/', views.add),
    path('add0/', views.add),
    path('', views.main_page),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
]
