from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Book, Rental
from django.contrib.auth.models import User
from .forms import BookForm, RentalForm
from django.http import JsonResponse
import logging
import os
from django.conf import settings

logger = logging.getLogger(__name__)

def book_list(request):
    books = Book.objects.all()
    users = User.objects.all()
    return render(request, 'book_list.html', {'books': books, 'users': users})

def rental_list(request):
    rentals = Rental.objects.all()
    return render(request, 'rental_list.html', {'rentals': rentals})

def create_rental(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            # manually getting the user and book objects from the request
            instance = form.save(commit=False)
            try:
                instance.user = User.objects.get(username=request.POST.get('user'))
                print(f"User: {instance.user}")
                instance.book = Book.objects.get(id=request.POST.get('book'))
                print(f"Book: {instance.book}")

                form.save()
                print(f"Rental created")
            
                return JsonResponse({'message': "Rental created successfully", 'status': 200})
            except:
                return JsonResponse({'error': 'Invalid user or book', 'status': 400})


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return JsonResponse({'message': 'Book created successfully', 'status': 200})
            except Exception as e:
                return JsonResponse({'error': str(e), 'status': 400})
        else:
            # Gives the form error
            return JsonResponse({'error': form.errors.as_json(), 'status': 400})

def delete_book(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        book.delete()
        return JsonResponse({'message': 'Book deleted successfully', 'status': 200})

def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book_cover_name = book.cover.name
    book_cover_name = book_cover_name.replace('/', '\\')

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            # Delete the old cover if a new one is sent
            if 'cover' in request.FILES:
                if book.cover:
                    old_cover = os.path.join(settings.MEDIA_ROOT, book_cover_name)
                    print(old_cover)
                    if os.path.exists(old_cover):
                        os.remove(old_cover)
            form.save()
            return JsonResponse({'message': 'Book updated successfully', 'status': 200})
        else:
            return JsonResponse({'error': form.errors.as_json(), 'status': 400})