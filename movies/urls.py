from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'movies'

# Adds url for pages to the site
urlpatterns = [
    path('', views.index, name='index'),

    path('search/', views.search_movie, name='search_movie'),

    path('vote/<int:movie_id>/', views.vote_movie, name='vote_movie'),

    path('register/', views.register_user, name='register'),

    path('login/', views.login_user, name='login'),

    path("logout/", views.logout_view, name="logout"),

    path("logged_out/", views.logged_out_view, name="logged_out"),

    path("about/", views.about_page, name="about"),

    # Test to check if API key was working
    #path('test-api/', views.test_api_key, name='test_api'),

    # Test to check if TMDB API integration was working
    #path('import/', views.import_movie),

]