from django.shortcuts import render, get_object_or_404
import requests
from django.http import HttpResponse
# Create your views here.

TMDB_API_KEY = "03848ea6b6db5941f9ee92f5f04801a2"


def search(request):
    
    # getting the query from the search box
    query = request.GET.get('q')

    if query:
        data = requests.get("https://api.themoviedb.org/3/search/movie?api_key=(TMBD_API_KEY)&include_adult=false&language=en-US&page=1&query=(query)")

    else:
        return HttpResponse("Please enter a search query")

    return render(request, 'blog/results.html', {
        data: data
    })


def index(request):
    return render(request, 'blog/index.html')
