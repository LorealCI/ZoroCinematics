from django.contrib import admin
from .models import Movie, Review
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
admin.site.register(Movie)
admin.site.register(Review)
