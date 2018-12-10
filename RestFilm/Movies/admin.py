from django.contrib import admin
from .models import Film, Comment, News

# Register your models here.
admin.site.register(Film)
admin.site.register(Comment)
admin.site.register(News)
