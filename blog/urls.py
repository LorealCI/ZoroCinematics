from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("movie/<int:movie_id>/", views.view_movie, name="view_movie"),
]
