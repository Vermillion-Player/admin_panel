from django.contrib import admin
from django.utils.html import format_html
from movie.models import *

admin.site.site_header = 'Peliculas'

class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "imagen", "name", "duration", "release_date", "channel", "only_adult")
    list_filter = ("name", "only_adult", "duration", "release_date", "channel", "only_adult")

    def imagen(self, obj):
        try:
            return format_html("<img src={} height='75' />", obj.image.url)
        except:
            return ""

admin.site.register(Movie, MovieAdmin)