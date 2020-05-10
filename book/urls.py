from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_book, name='view_book'),
    path('add/<item_id>/', views.add_to_book, name='add_to_book'),
]