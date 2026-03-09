from django.shortcuts import render, get_object_or_404
from .models import Page

def index(request, pagename=''):
    pagename = '/' + pagename
    pg = get_object_or_404(Page, permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.content,
        'page_list': Page.objects.all(),
    }
    return render(request, 'pages/page.html', context)