# coding: utf-8
from django.shortcuts import render
import random
from .models import Film
from .models import Comment
from .models import News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib import auth
from .forms import CommentForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.utils.translation import ugettext as _
from django.contrib import messages
from .forms import RegistrationForm
from .forms import ContactForm
from django.contrib.auth.models import User
from django.core.mail import send_mail


# Create your views here.
def home(request):
    movie_list = Film.objects.order_by("-created_on")
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

    return render(request, 'Movies/home.html', {'movie_list': movie_list, 'news_list': news_list, 'user': user, 'random_movie': random_movie})

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
    movie_list = Film.objects.order_by("-created_on")
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

    return render(request, 'Movies/filter.html', {'slug_meta': slug, 'news_list': news_list, 'random_movie': random_movie, 'user': user, 'movies': movies})

def signin(request):
    movie_list = Film.objects.all()
    random_movie = random.choice(movie_list)

    if request.method == 'POST':
        l_username = request.POST['username']
        l_password = request.POST['password']
        user = authenticate(request, username=l_username, password=l_password)

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/')
        else:
            messages.warning(request, 'Sorry, login or password was invalid. Please try again.')
            return HttpResponseRedirect(request.path_info)

    return render(request, 'Movies/signin.html', {'random_movie': random_movie})

def signup(request):
    movie_list = Film.objects.all()
    random_movie = random.choice(movie_list)

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            l_username = request.POST['username']
            l_password = request.POST['password1']
            user = authenticate(request, username=l_username, password=l_password)

            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()

    return render(request, 'Movies/signup.html', {'form': form, 'random_movie': random_movie})

def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/')

def contact(request):
    movie_list = Film.objects.all()
    random_movie = random.choice(movie_list)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']

            send_mail(subject, message, sender, ['viktorkozachok21@gmail.com'])
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()

    return render(request, 'Movies/send.html', {'form': form, 'random_movie': random_movie})
