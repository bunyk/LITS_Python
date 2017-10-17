from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404


from .models import Recipy, Product

def index(request):

    recipys = Recipy.objects.all()

    return render(request, 'fridge/index.html', {
        'recipys': recipys
    })

def products_by_ingredients(ingredients):
    ingredients = set(map(int, ingredients.split(',')))
    products = Product.objects.filter(pk__in=ingredients)
    for p in products:
        p.search_without = ','.join(str(i) for i in (ingredients - set([p.id])))

    more_products = Product.objects.exclude(pk__in=ingredients)
    for p in more_products:
        p.search_with = ','.join(str(i) for i in (ingredients | set([p.id])))
    return products, more_products, ingredients

def search(request, ingredients): 
    products, more_products, ingredients = products_by_ingredients(ingredients)

    recipys = Recipy.objects.raw('''
        select * from fridge_recipy where id not in (
            select recipy_id from fridge_ingredient
            where fridge_ingredient.product_id not in (%s)
        );
    ''' % ','.join(str(i) for i in ingredients));
    return render(request, 'fridge/index.html', {
        'products': products,
        'more_products': more_products,
        'recipys': recipys,
    })

def search_best(request, ingredients): 
    products, ingredients = products_by_ingredients(ingredients)

    recipys = Recipy.objects.raw('''
        select * from fridge_recipy where id not in (
            select recipy_id from fridge_ingredient
            where fridge_ingredient.product_id not in (%s)
        );
    ''' % ','.join(str(i) for i in ingredients));
    return render(request, 'fridge/index.html', {
        'products': products,
        'more_products': more_products,
        'recipys': recipys,
    })


def recipy(request, recipy_id): 
    recipy = get_object_or_404(Recipy, pk=recipy_id)
    ingredients = recipy.ingredient_set.all()
    return render(request, 'fridge/recipy.html', {
        'recipy': recipy,
        'ingredients': ingredients,
    })
