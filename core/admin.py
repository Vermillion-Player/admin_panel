from django.contrib import admin
from django.utils.html import format_html
from core.models import *

admin.site.site_header = 'General'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "imagen", "name", "only_adult")
    list_filter = ("name", "only_adult")

    def imagen(self, obj):
        try:
            return format_html("<img src={} height='75' />", obj.logo.url)
        except:
            return ""
        
class ActorAdmin(admin.ModelAdmin):
    list_display = ("id", "imagen", "name", "birthdate", "birthplace", "height", "weight", "genre", "only_adult")
    list_filter = ("name", "birthplace", "height", "weight", "genre", "only_adult")

    def imagen(self, obj):
        try:
            return format_html("<img src={} height='75' />", obj.image.url)
        except:
            return ""

admin.site.register(Category, CategoryAdmin)
admin.site.register(Actor, ActorAdmin)