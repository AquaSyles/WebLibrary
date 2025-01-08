from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('rentals/', views.rental_list, name='rental_list'),
    path('create_book/', views.create_book, name='create_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('update_book/<int:book_id>/', views.update_book, name='update_book'),
]