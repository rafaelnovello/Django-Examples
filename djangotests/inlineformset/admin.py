#coding: utf-8

from django.contrib import admin
from models import *


class BookInline(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        BookInline,
    ]

admin.site.register(Author, AuthorAdmin)
