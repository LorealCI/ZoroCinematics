from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Review
from .forms import ReviewForm
# Create your views here.


def home(request):
    items = Movie.objects.all()
    context = {
        'items': items
    }
    return render(request, 'blog/index.html', context)
