from django.contrib import admin
from program.models import *

admin.site.site_header = 'Programas'

admin.site.register(Program)
admin.site.register(Season)
admin.site.register(Episodes)