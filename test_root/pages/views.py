from django.shortcuts import render
from . models import Page

def index(request, pagename=''):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.content
    }
    return render(request, 'base.html', context)