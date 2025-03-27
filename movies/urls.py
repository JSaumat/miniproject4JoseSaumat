from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),

    path('search/', views.search_movie, name='search_movie'),

    path('vote/<int:movie_id>/', views.vote_movie, name='vote_movie'),

    path('register/', views.register_user, name='register'),

    path('login/', views.login_user, name='login'),

    path('logout/', views.logout_user, name='logout'),

    # Test to check if API key was working
    #path('test-api/', views.test_api_key, name='test_api'),

    # Test to check if TMDB API integration was working
    #path('import/', views.import_movie),

]