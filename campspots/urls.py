from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_campspots, name='campspots'),
    path('<int:campspot_id>/', views.campspot_detail, name='campspot_detail'),
    path('add/', views.add_campspot, name='add_campspot'),
    path('edit/<int:campspot_id>/', views.edit_campspot, name='edit_campspot'),
    path('delete/<int:campspot_id>/', views.delete_campspot, name='delete_campspot'),
    ]
