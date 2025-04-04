import requests

from django.conf import settings

def search_tmdb(query):
    url = f"https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": settings.TMDB_API_KEY,
        "query": query
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get("results", [])[:12]  # Return top 6 results
    return []