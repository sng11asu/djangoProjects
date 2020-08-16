from django.contrib import admin

from .models import Collections, Counter, Genres, Movies

# Register your models here.
admin.site.register(Collections)
admin.site.register(Counter)
admin.site.register(Movies)
admin.site.register(Genres)
