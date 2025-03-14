from django.contrib import admin
from .models import Review

# Register your models here.


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'movie_id', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'text')

