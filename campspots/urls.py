from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_campspots, name='campspots'),
    path('<campspot_id>', views.campspot_detail, name='campspot_detail'),
    # path('date/', views.product_date, name='product_date'),
    # path('add_date/', views.add_date, name='add_date'),
    # path('<int:campspot_id>/', views.campspot_detail, name='campspot_detail'),
    # path('add/', views.add_product, name='add_product'),
    # path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    # path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    ]