from django.urls import path
from . import views

urlpatterns = [
    path('rentals/', views.rental_list, name='rental_list'),
    path('create_rental/', views.create_rental, name='create_rental'),
    path('delete_rental/<int:rental_id>/', views.delete_rental, name='delete_rental'),
    path('books/', views.book_list, name='book_list'),
    path('search_book/', views.search_book, name='search_book'),
    path('create_book/', views.create_book, name='create_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('update_book/<int:book_id>/', views.update_book, name='update_book'),
]