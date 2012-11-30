from django.db import models
from django.forms import ModelForm


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=100)


class AuthorForm(ModelForm):
    class Meta:
        model = Author
