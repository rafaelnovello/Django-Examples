#coding:utf-8

from models import Author, Book, AuthorForm

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.forms.models import inlineformset_factory
from django.views.generic.list_detail import object_list


def authors_list(request):
    authors = Author.objects.all()
    return object_list(request, queryset=authors, template_name="author_list.html")


def author_delete(request, pk):
    Author.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/inlines/')


def author_add(request):
    author = Author()
    return author_manager(request, author)


def author_edit(request, pk):
    author = Author.objects.get(pk=pk)
    return author_manager(request, author)


def author_manager(request, author):
    BookInlineFormSet = inlineformset_factory(Author, Book, extra=1,
                                              formfield_callback=add_category)

    form = AuthorForm(request.POST or None, instance=author)
    formset = BookInlineFormSet(request.POST or None, instance=author)

    if form.is_valid() and formset.is_valid():
        form.save()
        formset.save()
        return HttpResponseRedirect('/inlines/')

    return render_to_response("manage_authors.html",
        {"formset": formset,
        "form": form},
        RequestContext(request))


def add_category(field, **kwargs):
        if field.name == 'category':
            additional_choices = [
                    ('best_seller', 'Best Seller'),
                    ('self_help', 'Auto Ajuda')
                ]
            for choice in additional_choices:
                if not choice in field.choices:
                    field.choices.extend(additional_choices)
        return field.formfield(**kwargs)
