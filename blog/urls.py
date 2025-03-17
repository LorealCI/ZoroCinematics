from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/", include("allauth.urls")),
    path("search/", views.search, name="search"),
    path("movie/<int:movie_id>/", views.view_movie, name="view_movie"),
    path("review/update/<int:review_id>/", views.update_review, name="update_review"),
    path("review/delete/<int:review_id>/", views.delete_review, name="delete_review"),
    path("trending/", views.view_trending, name="view_trending"),
]
