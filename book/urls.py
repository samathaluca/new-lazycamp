from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_book, name='view_book'),
    path('add/<item_id>/', views.add_to_book, name='add_to_book'),
    path('adjust/<item_id>/', views.adjust_book, name='adjust_book'),
    path('remove/<item_id>/<date>', views.remove_from_book_ajax, name='remove_from_book'),
    path('remove_and_rebook/<item_id>/<date>', views.remove_and_rebook, name='remove_and_rebook'),
    # path('remove/<item_id>/<date>', views.remove_and_rebook, name='remove_and_rebook'),
]