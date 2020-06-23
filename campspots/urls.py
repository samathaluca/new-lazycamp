from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_campspots, name='campspots'),
    # path('<int:campspot_id>/', views.campspot_detail, name='campspot_detail'),
    path('<int:campspot_id>/', views.campspot_detail, name='campspot_detail'),
]