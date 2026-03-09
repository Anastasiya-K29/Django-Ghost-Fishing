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

def ghost_gear(request, material, weight, years):
    
    # Material types
    materials = {
        1: ('Nylon', 600),
        2: ('Polyester', 400),
        3: ('Metal', 200),
    }

    # Default to nylon if invalid material number entered
    material_name, base_years = materials.get(material, ('Unknown Material', 500))

    # Calculate how long gear will remain active
    remaining_years = max(0, base_years - years)

    # Calculate estimated animals trapped per year based on weight
    animals_per_year = weight * 12

    # Total estimated animals trapped so far
    total_animals = animals_per_year * years

    # Calculate damage level
    if remaining_years > 300:
        damage_level = 'Catastrophic'
        damage_colour = 'red'
    elif remaining_years > 100:
        damage_level = 'Severe'
        damage_colour = 'orange'
    elif remaining_years > 50:
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