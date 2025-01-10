from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Book, Rental
from django.contrib.auth.models import User
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
        form = RentalForm(request.POST)
        if form.is_valid():
            # manually getting the user and book objects from the request
            instance = form.save(commit=False)
            try:
                instance.user = User.objects.get(id=request.POST.get('user'))
                print(f"User: {instance.user}")
                instance.book = Book.objects.get(id=request.POST.get('book'))
                print(f"Book: {instance.book}")

                form.save()
                print(f"Rental created")
            except:
                return JsonResponse({'error': 'Invalid user or book'}, status=400)


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