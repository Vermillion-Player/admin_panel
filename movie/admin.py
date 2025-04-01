from django.contrib import admin
from movie.models import *

admin.site.site_header = 'Peliculas'

admin.site.register(Movie)