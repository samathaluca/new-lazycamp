from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_book, name='view_book'),
    path('add/<item_id>/', views.add_to_book, name='add_to_book'),
    path('adjust/<item_id>/', views.adjust_book, name='adjust_book'),
    path('remove/<item_id>/<date>', views.remove_from_book, name='remove_from_book'),
]