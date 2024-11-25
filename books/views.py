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
    q = request.GET.get("q")

    if q:
        books = Book.objects.filter(title__icontains=q)
        context = {"books": books}
    else:
        books = Book.objects.all()
        context = {"books": books, "query": q}

    return render(request, "books/book_list.html", context)


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, "books/book_detail.html", {"book": book})
