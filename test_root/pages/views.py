from django.shortcuts import render, get_object_or_404
from .models import Page

def index(request, pagename=''):
    pagename = '/' + pagename
    pg = get_object_or_404(Page, permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.content,
        'page_list': Page.objects.all(),
        'authors': pg.authors,
        'references': pg.references,
        'permalink': pg.permalink,
    }
    return render(request, 'base.html', context)

def ghost_gear(request, material, weight, years):
    
    materials = {
        1: ('Nylon', 600),
        2: ('Polyester', 400),
        3: ('Metal', 200),
    }

    material_name, base_years = materials.get(material, ('Unknown Material', 500))

    remaining_years = max(0, base_years - years)

    animals_per_year = weight * 12

    total_animals = animals_per_year * years

    if total_animals >= 10000:
        damage_level = 'Catastrophic'
        damage_colour = 'red'
    elif total_animals >= 1000:
        damage_level = 'Severe'
        damage_colour = 'orange'
    elif total_animals >= 100:
        damage_level = 'Moderate'
        damage_colour = 'yellow'
    else:
        damage_level = 'Low'
        damage_colour = 'green'

    context = {
        'title': 'Ghost Gear Calculator',
        'material': material,
        'material_name': material_name,
        'weight': weight,
        'years': years,
        'remaining_years': remaining_years,
        'animals_per_year': animals_per_year,
        'total_animals': total_animals,
        'damage_level': damage_level,
        'damage_colour': damage_colour,
        'base_years': base_years,
    }
    return render(request, 'pages/ghost_gear.html', context)

def request_info(request):
    submitted = False

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        topic = request.POST.get("topic")
        message = request.POST.get("message")

        submitted = True

    context = {
        "title": "Request Further Information",
        "submitted": submitted,
        "page_list": Page.objects.all(),
    }

    return render(request, "pages/request_info.html", context)