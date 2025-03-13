from django.shortcuts import render, get_object_or_404
from django.conf import settings
import requests
from django.http import HttpResponse
# Create your views here.


def search(request):
    
    # getting the query from the search box
    query = request.GET.get('q')
    print(query)

    if query:
        data = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={settings.TMDB_API_KEY}&include_adult=false&language=en-US&page=1&query={query}")
        print(data.json())

    else:
        return HttpResponse("Please enter a search query")

    return render(request, 'blog/results.html', {
        "data": data.json(),
        "type": request.GET.get("type"),
    })


def index(request):
    return render(request, 'blog/index.html')


def view_movie(request, movie_id):
    data = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={settings.TMDB_API_KEY}&include_adult=false&language=en-US")
    recommendations = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={settings.TMDB_API_KEY}&include_adult=false&language=en-US")
    return render(request, "blog/movies.html", {
        "data": data.json(),
        "recommendations": recommendations.json(),
        "type": "movie",
    })
