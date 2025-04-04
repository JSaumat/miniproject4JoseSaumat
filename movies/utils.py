import requests
from django.conf import settings

# Custom model to store movies
from .models import Movie

# Created a reusable script that can pull data from the TMDB API
def fetch_and_save_movie(title):

    url = f"https://api.themoviedb.org/3/search/movie?api_key={settings.TMDB_API_KEY}&query={title}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        results = data.get("results")

        if results:
            movie_data = results[0] # Gets the first matching result
            tmdb_id = movie_data["id"]

            # Creates and saves the movie in the local database
            movie = Movie.objects.create(

                title=movie_data["title"],
                tmdb_id=tmdb_id,
                poster_url=f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}" if movie_data.get("poster_path") else "",
                description=movie_data.get("overview", ""),
                release_date=movie_data.get("release_date", None)

            )

            return movie

    return None # Returns nothing if movie was not found
