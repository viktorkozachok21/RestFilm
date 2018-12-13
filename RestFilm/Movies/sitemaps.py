from django.contrib.sitemaps import Sitemap
from .models import Film
from django.urls import reverse


class FilmSitemap(Sitemap):
    changfreq = "daily"
    priority = 1.0

    def items(self):
        return Film.objects.all()

    def location(self, obj):
        return "/film/{0}/".format(obj.title)


class StaticViewSitemap(Sitemap):

    def items(self):
        return ['home', 'signin', 'signup', 'userlogout', 'contact']

    def location(self, item):
        return reverse(item)
