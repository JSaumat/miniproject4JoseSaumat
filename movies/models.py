from django.db import models

# Create your models here.

# Movie model represents each movie record saved in the database
class Movie(models.Model):

    # Movie title
    title = models.CharField(max_length=200)

    # TMDB's unique ID for each movie
    tmdb_id = models.IntegerField(unique=True)

    # Link to movies movie poster if available
    poster_url = models.URLField(blank=True)

    # Link to movie description
    description = models.TextField(blank=True)

    # Link to movie release date
    release_date = models.DateField(null=True, blank=True)

    # Total number of votes cast by the members of the site
    vote_count = models.IntegerField(default=0)

    # Defines how the object appears
    def __str__(self):
        return self.title