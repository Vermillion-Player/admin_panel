from django.contrib import admin
from channel.models import *

admin.site.site_header = 'Canales'
admin.site.index_title = 'Administración de Canales'
admin.site.site_title = 'Canales'

admin.site.register(Channel)

