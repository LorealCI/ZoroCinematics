from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http.response import JsonResponse
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.db.models import Avg
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

    # Calculate remaining stars for each review
    # for review in review:
    #    review.remaining_stars = 5 - review.rating

    # Calculate average rating
    average_rating = review.aggregate(Avg('rating'))['rating__avg']

    return render(request, "blog/movies.html", {
        "data": data.json(),
        "recommendations": recommendations.json(),
        "form": form,
        "reviews": review,
        "average_rating": round(average_rating, 1) if average_rating else None,
        "type": "movie",
    })


# def fetch_movie_data(movie_id):
#   url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={settings.TMDB_API_KEY}&include_adult=false&language=en-US"
#  response = requests.get(url)
#    if response.status_code == 200:
#        return response.json()
#    else:
#        return {"error": "Failed to fetch movie data"}


# def view_movie_data(request, movie_id):
#    movie_data = fetch_movie_data(movie_id)
#    reviews = Review.objects.filter(movie_id=movie_id)
#    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']

#    context = {
#        'data': movie_data,
#        'reviews': reviews,
#        'average_rating': round(average_rating, 1) if average_rating else None,  # Rounds it to 1 decimal place
#    }
#    return render(request, 'blog/movies.html', context)


def update_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    # Ensure that only the owner of the review can update it
    if review.name != request.user:
        return HttpResponseForbidden("You are not allowed to edit this review.")

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('view_movie', movie_id=review.movie_id)


def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    # Ensure that only the owner of the review can delete it
    if review.name != request.user:
        return HttpResponseForbidden("You are not allowed to delete this review.")

    if request.method == 'POST':
        movie_id = review.movie_id
        review.delete()
        return redirect('view_movie', movie_id=movie_id)


def view_trending(request):
    url = f"https://api.themoviedb.org/3/trending/movie/week?api_key={settings.TMDB_API_KEY}&include_adult=false&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Failed to fetch trending movies"}, status=response.status_code)


# def autocomplete_search(request):
    # query = request.GET.get('q', '')  # Get the query from the request
    # if query:
    # url = f"https://api.themoviedb.org/3/search/movie?api_key={settings.TMDB_API_KEY}&query={query}&include_adult=false&language=en-US&page=1"
    # response = requests.get(url)
    # if response.status_code == 200:
        #    results = response.json().get('results', [])
        #    suggestions = [{'id': movie['id'], 'title': movie['title']} for movie in results[:10]]  # Limit to 10 suggestions
        #    return JsonResponse(suggestions, safe=False)
# return JsonResponse([], safe=False)
