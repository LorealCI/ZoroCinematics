from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewer")
    comment = models.TextField()
    movie_id = models.IntegerField()
    ratings = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    stars = models.IntegerField(choices=ratings)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.movie.title
