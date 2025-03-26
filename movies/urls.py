from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),

    # Test to check if API key was working
    #path('test-api/', views.test_api_key, name='test_api'),

    # Test to check if TMDB API integration was working
    #path('import/', views.import_movie),



]