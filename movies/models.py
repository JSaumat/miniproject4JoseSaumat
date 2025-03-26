from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    tmdb_id = models.IntegerField(unique=True)
    poster_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    release_date = models.DateField(null=True, blank=True)
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title