import uuid

from django.db import models


class Genres(models.Model):
    genre = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.genre}"

class Movies(models.Model):
    movie_uuid = models.CharField(max_length=50)
    genre = models.ManyToManyField(Genres, blank=True, related_name='movie')
    def __str__(self):
        return f"{self.movie_uuid}"

class Collections(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    movies = models.ManyToManyField(Movies, blank=True, related_name='collection')
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return f"{self.title}"
    
class Counter(models.Model):
    status = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.status}"
