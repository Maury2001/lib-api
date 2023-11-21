from django.shortcuts import render
from django.views.generic import ListView

from .models import Book

# Create your views here.
def Home(request):
    books = Book.objects.all()

    context={
        'books': books
    }

    return render(request, 'books/book_list.html', context)
