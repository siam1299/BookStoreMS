from django.shortcuts import render, redirect
from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, "books/book_list.html", {"books": books})
