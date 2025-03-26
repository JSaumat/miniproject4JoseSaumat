from django.shortcuts import render

from django.http import HttpResponse
from django.conf import settings

# Used to test TMDB API integration
# from .utils import fetch_and_save_movie

# Create your views here.
def index(request):
    return render(request, 'movies/index.html')

# Test to see if API key was working
# def test_api_key(request):
#     return HttpResponse(f"API Key: {settings.TMDB_API_KEY}")

# Used to test TMDB API integration
# def import_movie(request):
#     movie = fetch_and_save_movie("The Matrix")
#     if movie:
#         return HttpResponse(f"Imported movie: {movie.title}")
#     return HttpResponse("Movie not found.")

