from django.urls import path
from . import views
from .decorators import check_recaptcha
from django.contrib.sitemaps.views import sitemap

from Movies.sitemaps import FilmSitemap, StaticViewSitemap

sitemaps = {
    'films': FilmSitemap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.home, name="home"),
    path('film/<slug>', check_recaptcha(views.watch), name="watch"),
    path('search/<slug>', views.filter, name="filter"),
    path('account/login', check_recaptcha(views.signin), name="signin"),
    path('account/registration', check_recaptcha(views.signup), name="signup"),
    path('account/logout', views.userlogout, name="userlogout"),
    path('contact/send', check_recaptcha(views.contact), name="contact"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='cached-sitemap'),
]
