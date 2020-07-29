from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    # path('date/', views.product_date, name='product_date'),
    path('add_date/', views.add_date, name='add_date'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('messenging/', views.messenging, name='messenging'),
    path('contact/', views.contact, name='contact'),
    ]