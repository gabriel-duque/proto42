from django.contrib import admin

from backend.models import Artist, Song, Album, Genre

admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Genre)
