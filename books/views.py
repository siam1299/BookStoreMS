from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from orders.models import OrderItem
from .forms import BookForm, ReviewForm
from .models import Book, Review


# Create your views here.
def add_book(request):
    # only superusers can add books
    if not request.user.is_superuser:
        return redirect("home")

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
    # get all reviews for this book
    reviews = Review.objects.filter(book=book)
    # check if the book is purchased by the user
    is_purchased = check_purchased(request, pk)

    form = ReviewForm()
    return render(
        request,
        "books/book_detail.html",
        {"book": book, "form": form, "reviews": reviews, "is_purchased": is_purchased},
    )


@login_required
def add_book_review(request, pk):
    print(request.POST)
    # Check if user has purchased this book
    purchased = check_purchased(request, pk)

    if not purchased:
        return redirect("book_detail", pk=pk)

    # if purchased, add review
    book = Book.objects.get(pk=pk)
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.book = book
        review.user = request.user
        review.save()
    return redirect("book_detail", pk=pk)


def check_purchased(request, book_pk):
    return OrderItem.objects.filter(order__customer__user=request.user, book__pk=book_pk).exists()
