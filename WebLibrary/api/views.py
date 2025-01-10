from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Book, Rental
from .forms import BookForm, RentalForm
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def rental_list(request):
    rentals = Rental.objects.all()
    return render(request, 'rental_list.html', {'rentals': rentals})

@csrf_exempt
def create_rental(request):
    if request.method == 'POST':
        print(request.POST)
        form = RentalForm(request.POST)
        print(form)
        if form.is_valid():
            print("VALID")
            form.save()

@csrf_exempt
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return JsonResponse({'message': 'Book created successfully'}, status=200)
            except Exception as e:
                logger.error(f"Error creating book: {e}")
                return JsonResponse({'error': str(e)}, status=400)
        else:
            return JsonResponse({'error': form.errors.as_json()}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def delete_book(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        book.delete()
        return JsonResponse({'message': 'Book deleted successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Book updated successfully'}, status=200)
        else:
            return JsonResponse({'error': form.errors.as_json()}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)