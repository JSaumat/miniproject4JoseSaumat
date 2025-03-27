from django.shortcuts import render

from .forms import MovieSearchForm

from .utils import fetch_and_save_movie

from .models import Movie

from django.shortcuts import get_object_or_404, redirect

from django.db.models import F

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

# Creates the view to search for movies
def search_movie(request):
    form = MovieSearchForm()
    message = ""

    if request.method == "POST":
        form = MovieSearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            movie = fetch_and_save_movie(title)
            if movie:
                message = f"Movie '{movie.title}' imported successfully!"
            else:
                message = "Movie not found or could not be imported."

    return render(request, "movies/search.html", {"form": form, "message": message})

# Adds the movie view in index
def index(request):
    movies = Movie.objects.all().order_by('-release_date')
    return render(request, 'movies/index.html', {'movies': movies})

# Adds the voting view
def vote_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.vote_count = F('vote_count') + 1
    movie.save()
    movie.refresh_from_db()  # Refresh to get updated vote_count
    return redirect('movies:index')  # Go back to home page

