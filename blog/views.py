from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Review
# Create your views here.


def home(request):
    items = Movie.objects.all()
    context = {
        'items': items
    }
    return render(request, context)

def my_blog(request):
    return HttpResponse("Welcome to my blog!")