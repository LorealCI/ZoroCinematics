from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Comment'}),
        }