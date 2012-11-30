#coding:utf-8

from models import Author, Book

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.forms.models import inlineformset_factory
from django.forms.models import modelformset_factory


def manage_authors(request):
    AuthorFormSet = modelformset_factory(Author, can_delete=True, extra=0)
    if request.method == 'POST':
        if 'add_author' in request.POST:
            cp = request.POST.copy()
            cp['form-TOTAL_FORMS'] = int(cp['form-TOTAL_FORMS']) + 1
            formset = AuthorFormSet(cp)
        elif 'submit' in request.POST:
            formset = AuthorFormSet(request.POST, request.FILES)
            if formset.is_valid():
                formset.save()
                # do something.
    else:
        formset = AuthorFormSet()
    return render_to_response("manage_authors.html",
        {"formset": formset},
         RequestContext(request))


def add_books(request, author_id):
    author = Author.objects.get(pk=author_id)
    BookInlineFormSet = inlineformset_factory(Author, Book, extra=0)
    if request.method == "POST":
        if 'add_title' in request.POST:
            cp = request.POST.copy()
            cp['book_set-TOTAL_FORMS'] = int(cp['book_set-TOTAL_FORMS']) + 1
            formset = BookInlineFormSet(cp, instance=author)
        elif 'submit' in request.POST:
            formset = BookInlineFormSet(request.POST, request.FILES, instance=author)
            if formset.is_valid():
                formset.save()
                return HttpResponseRedirect('/inlines/author/1/books/add/')
    else:
        formset = BookInlineFormSet(instance=author)
    return render_to_response("inline.html",
        {"formset": formset},
        RequestContext(request))
