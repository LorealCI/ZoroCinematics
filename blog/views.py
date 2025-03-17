from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
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
    
    # Handle comment form submission
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie_id = movie_id
            review.name = request.user  # Associates the review with the logged-in user
            review.save()
            return redirect('view_movie', movie_id=movie_id)  # This redirects to the same page after submit
    else:
        form = ReviewForm()

    # Fetch all comments for the current movie
    review = Review.objects.filter(movie_id=movie_id).order_by('-created_at')

    return render(request, "blog/movies.html", {
        "data": data.json(),
        "recommendations": recommendations.json(),
        "form": form,
        "reviews": review,
        "type": "movie",
    })


def view_trending(request):
    url = f"https://api.themoviedb.org/3/trending/movie/week?api_key={settings.TMDB_API_KEY}&include_adult=false&language=en-US"
    response = requests.get(url)
    return JsonResponse(response.json())
