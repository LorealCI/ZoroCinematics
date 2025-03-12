from django.shortcuts import render
from .models import Movie, Review
from .forms import ReviewForm
# Create your views here.


def home(request):
    items = Movie.objects.all()
    context = {
        'items': items
    }
    return render(request, 'blog/index.html', context)


def rate(request, id):
    post = Movie.objects.get(id=id)
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        author = request.POST.get('author')
        stars = request.POST.get('stars')
        comment = request.POST.get('comment')
        review = Review(author=author, stars=stars,  comment=comment, movie=post)
        review.save()
        return redirect('success')

    form = ReviewForm()
    context = {
        "form": form

    }
    return render(request, context)
