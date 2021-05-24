from django.contrib import admin
from django.urls import path
from dz1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.get_all_products),
    path('products/<int:id>/', views.get_one_product),
    path('products/', views.get_all_products)
    # path('add/', views.add)
]
