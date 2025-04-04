# Used to make requests from the TMDB API
import requests

# Used to access TMDB API key from settings.py
from django.conf import settings

# Search TMDB for a movie by title in the navigation bar (quick lookup version)
def search_tmdb(query):

    url = f"https://api.themoviedb.org/3/search/movie"

    params = {

        "api_key": settings.TMDB_API_KEY,
        "query": query

    }

    response = requests.get(url, params=params)

    if response.status_code == 200:

        #Parses JSON response and display top 12 results
        data = response.json()

        return data.get("results", [])[:12]  # Return top 12 results

    return [] # If the API call fails