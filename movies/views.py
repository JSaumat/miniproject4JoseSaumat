from django.shortcuts import render

from .forms import MovieSearchForm

from .utils import fetch_and_save_movie

from .models import Movie

from django.shortcuts import get_object_or_404, redirect

from django.db.models import F

from django.contrib.auth import login, authenticate, logout

from .forms import RegisterForm, LoginForm

from django.contrib import messages

from django.shortcuts import redirect

from django.contrib.auth.decorators import user_passes_test

from django.http import HttpResponse

from django.conf import settings

from django.core.exceptions import PermissionDenied

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

# Checks to make sure user is authorized to access page if not throws 403 error
def only_admin(user):
    if not user.is_authenticated or not (user.is_superuser or user.is_staff):
        raise PermissionDenied
    return True

# Creates the view to search for movies that only superusers or admins can access
@user_passes_test(only_admin)
def search_movie(request):
    form = MovieSearchForm()
    message = ""

    if request.method == "POST":
        # Handles submission from either the MovieSearchForm or the navbar input
        title = request.POST.get("title")
        if title:
            movie = fetch_and_save_movie(title)
            if movie:
                message = f"Movie '{movie.title}' imported successfully!"
            else:
                message = "Movie not found or could not be imported."
        else:
            message = "Please enter a movie title."

    return render(request, "movies/search.html", {"form": form, "message": message})

# Adds the movie view in index
def index(request):
    movies = Movie.objects.all().order_by('-release_date')
    voted_movie = request.session.pop('voted', None)  # ✅ get + clear session
    login_required = request.session.pop('login_required', False)
    return render(request, 'movies/index.html', {
        'movies': movies,
        'voted_movie': voted_movie,
        'login_required': login_required
    })

# Adds the voting view
def vote_movie(request, movie_id):
    # Requires user to be logged in to vote
    if not request.user.is_authenticated:
        request.session['login_required'] = True
        return redirect('movies:index')

    movie = get_object_or_404(Movie, id=movie_id)
    movie.vote_count = F('vote_count') + 1
    movie.save()
    movie.refresh_from_db()  # Refresh to get updated vote_count
    request.session['voted'] = movie.title  # ✅ set session key
    return redirect('movies:index')  # Go back to home page

# Adds the registration view
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('movies:login')
    else:
        form = RegisterForm()
    return render(request, 'movies/register.html', {'form': form})

# Adds the log-in user view
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect('movies:index')
    else:
        form = LoginForm()
    return render(request, 'movies/login.html', {'form': form})

# Adds the log-out user view
def logout_view(request):
    logout(request)
    return redirect("movies:logged_out")

# Adds logged out page confirmation
def logged_out_view(request):
    return render(request, "movies/logged_out.html")