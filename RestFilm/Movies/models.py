# coding: utf-8
from django.db import models
from django.utils import timezone
from tinymce import HTMLField

# Create your models here.
class Film(models.Model):
    film_name = models.CharField(max_length=256,blank=False,null=False)
    title = models.CharField(max_length=256,blank=False,null=False)
    film_url = models.CharField(max_length=256,blank=False,null=False)
    trailer_url = models.CharField(max_length=256,blank=False,null=False)
    top = models.BigIntegerField()
    photo = models.ImageField()
    description = HTMLField('Description')
    content = HTMLField('Content')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=256)
    content = models.TextField(blank=False,null=False)
    post = models.ForeignKey(Film,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.author

class News(models.Model):
    title = models.CharField(max_length=256,blank=False,null=False)
    photo = models.ImageField()
    content = HTMLField('Content')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
