from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Review(models.Model):
    movie_id = models.IntegerField()
    name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review by {self.name.username} on Movie {self.movie_id}"
