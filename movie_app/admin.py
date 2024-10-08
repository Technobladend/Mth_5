from django.contrib import admin
from . import models


class ReviewInline(admin.StackedInline):
    model = models.Review
    extra = 1


class MovieAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]


admin.site.register(models.Director)

admin.site.register(models.Movie, MovieAdmin)

admin.site.register(models.Review)
