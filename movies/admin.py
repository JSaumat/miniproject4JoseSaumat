from django.contrib import admin

from .models import Movie

# Change admin site headers
admin.site.site_header = "MovieVote Admin"
admin.site.site_title = "MovieVote Admin Portal"
admin.site.index_title = "Welcome to the MovieVote Management Area"

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'vote_count')
    search_fields = ('title',)