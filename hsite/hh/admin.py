from django.contrib import admin
# @admin.register(Movie)
# @admin.register(Celebrities)
from .models import *


class MovieAdmin(admin.ModelAdmin):
    list_display = ('movieid', 'title', 'year', 'image'
                     , 'is_published'
                    )
    list_display_links = ('movieid', 'title')
    search_fields = ('title', 'year')
    prepopulated_fields = {'slug': ('title', 'year')}


admin.site.register(Movie)


class CelebritiesAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )
    date_hierarchy = 'date_of_birth'



admin.site.register(Celebrities)
