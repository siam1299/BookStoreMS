from django import forms
from .models import Book, Review


class BookForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 4}))

    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "publisher",
            "price",
            "points",
            "stock",
            "image",
            "category",
            "description",
        ]


class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows": 4}))

    class Meta:
        model = Review
        fields = ["stars", "text"]
