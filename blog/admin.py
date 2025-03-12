from django.contrib import admin
from .models import Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
admin.site.register(Comment)
