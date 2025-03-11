from django.urls import path
from .views import home, my_blog

urlpatterns = [
    path('', home, name='home'),
    path('blog/', my_blog, name='blog'),
]