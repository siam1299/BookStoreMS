from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book


# Create your views here.
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "books/book_form.html", {"form": form})


def book_list(request):
    books = Book.objects.all()
    return render(request, "books/book_list.html", {"books": books})
