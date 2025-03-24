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

    for r in review:
        r.rating_range = range(r.rating)
        r.remaining_range = range(5 - r.rating)

    total_ratings = sum(r.rating for r in review)
    num_reviews = review.count()
    average_rating = total_ratings / num_reviews if num_reviews > 0 else 0

    # Calculate the number of full, half, and empty stars
    full_stars = int(average_rating)  # Full stars (integer part of the rating)
    half_star = 1 if average_rating % 1 >= 0.5 else 0  # Half star if there's a decimal part >= 0.5
    empty_stars = 5 - full_stars - half_star

    star_representation = (
        "&#9733;" * full_stars +  # Full stars
        ("&#9733;" if half_star else "") +  # Half star if applicable
        "&#9734;" * empty_stars) # Empty stars

    return render(request, "blog/movies.html", {
        "data": data.json(),
        "recommendations": recommendations.json(),
        "form": form,
        "reviews": review,
        'average_rating': average_rating,
        'star_representation': star_representation,
        "type": "movie",
    })


def update_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    # Ensure that only the owner of the review can update it
    if review.name != request.user:
        return HttpResponseForbidden("You are not allowed to edit this review.")

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            # Return a JSON response for AJAX requests
            return JsonResponse({'success': True, 'message': 'Review updated successfully!'})
        else:
            # Return form errors for AJAX requests
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)

    # If the request is not POST, return a 405 Method Not Allowed response
    return JsonResponse({'error': 'Invalid request method'}, status=405)

           # return redirect('view_movie', movie_id=review.movie_id)
    

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
