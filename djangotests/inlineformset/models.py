#coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    CATEGORIES = [
        ('romance', 'Romance'),
        ('fiction', 'Ficção'),
        ('suspense', 'Suspense')
    ]
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORIES)


class AuthorForm(ModelForm):
    class Meta:
        model = Author
