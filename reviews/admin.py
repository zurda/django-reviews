from django.contrib import admin

from .models import Title, Review

admin.site.register([Title, Review])