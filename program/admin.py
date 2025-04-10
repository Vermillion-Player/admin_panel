from django.contrib import admin
from django.utils.html import format_html
from program.models import *

admin.site.site_header = 'Programas'

class ProgramAdmin(admin.ModelAdmin):
    list_display = ("id", "imagen", "name", "age", "main_category", "release_date", "channel")
    list_filter = ("name", "age", "main_category", "release_date", "channel")

    def imagen(self, obj):
        try:
            return format_html("<img src={} height='75' />", obj.image.url)
        except:
            return ""

class SeasonmAdmin(admin.ModelAdmin):
    list_display = ("id", "imagen", "name", "program", "release_date")
    list_filter = ("name", "program", "release_date")

    def imagen(self, obj):
        try:
            return format_html("<img src={} height='75' />", obj.image.url)
        except:
            return ""
        
class EpisodesAdmin(admin.ModelAdmin):
    list_display = ("id", "imagen", "name", "duration", "program", "season", "release_date")
    list_filter = ("name", "duration", "program", "season", "release_date")

    def imagen(self, obj):
        try:
            return format_html("<img src={} height='75' />", obj.image.url)
        except:
            return ""

admin.site.register(Program, ProgramAdmin)
admin.site.register(Season, SeasonmAdmin)
admin.site.register(Episodes, EpisodesAdmin)