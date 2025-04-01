from django.contrib import admin
from core.models import *

admin.site.site_header = 'General'

admin.site.register(Category)
admin.site.register(Actor)