from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Comment'}),
            'rating': forms.Select(attrs={'class': 'form-control'}, choices=[(i, f"{i} Stars") for i in range(1, 6)]),
        }
