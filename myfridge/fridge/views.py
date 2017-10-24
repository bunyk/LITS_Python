from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist


from .models import Recipy, Product, Comment

def index(request):
    recipys = Recipy.objects.all()

    return render(request, 'fridge/index.html', {
        'recipys': recipys,
        'user': request.user,
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

    if request.method == 'POST':
        text = request.POST['comment_text']
        user = request.user

        comment = Comment(author = user, text = text, recipy = recipy)
        comment.save()

    return render(request, 'fridge/recipy.html', {
        'recipy': recipy
    })
