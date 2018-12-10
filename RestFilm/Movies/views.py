# coding: utf-8
from django.shortcuts import render, redirect
import random
from .models import Film
from .models import Comment
from .models import News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.mail import send_mail
from .forms import CommentForm
from django.utils.translation import ugettext as _


# Create your views here.
def home(request):
    movie_list = Film.objects.all()
    news_list = News.objects.all()
    random_movie = random.choice(movie_list)
    user = auth.get_user(request)

    paginator = Paginator(movie_list, 6)
    page = request.GET.get('page')
    try:
        movie_list = paginator.page(page)
    except PageNotAnInteger:
        movie_list = paginator.page(1)
    except EmptyPage:
        movie_list = paginator.page(paginator.num_pages)

    return render(request, 'Movies/home.html', {'news_list': news_list, 'user': user, 'movie_list': movie_list, 'random_movie': random_movie})

def watch(request, slug):
    movie_list = Film.objects.all()
    random_movie = random.choice(movie_list)

    movie = Film.objects.get(title=slug)
    user = auth.get_user(request)

    content = ''

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.content = form.cleaned_data['content']
            comment.post = movie
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()

    comment = Comment.objects.filter(post=movie)

    return render(request, 'Movies/watch.html', {'form': form, 'content': content, 'user': user, 'comment': comment, 'movie': movie, 'random_movie': random_movie})

def filter(request, slug):
    movies = []
    movie_list = Film.objects.all()
    news_list = News.objects.all()

    if slug == _("Novelty"):
        for movie in movie_list:
            if movie.created_on.year >= 2018:
                movies.append(movie)
    elif slug == _("Popular"):
        for movie in movie_list:
            if movie.top >= 500:
                movies.append(movie)
    elif slug == 'result' and request.method == "GET":
        search = request.GET['search']
        for movie in movie_list:
            if search in movie.description or search in movie.content or search in movie.film_name:
                movies.append(movie)
    else:
        for movie in movie_list:
            if slug in movie.description or slug in movie.content:
                movies.append(movie)

    random_movie = random.choice(movie_list)
    user = auth.get_user(request)

    paginator = Paginator(movies, 6)
    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)

    return render(request, 'Movies/filter.html', {'news_list': news_list, 'random_movie': random_movie, 'user': user, 'movies': movies})
