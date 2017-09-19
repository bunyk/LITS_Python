from django.contrib import admin

from .models import Ingredient, Product, Recipy

class IngredientInline(admin.StackedInline):
    model = Ingredient
    extra = 5

class RecipyAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]

admin.site.register(Ingredient)
admin.site.register(Product)
admin.site.register(Recipy, RecipyAdmin)
# Register your models here.
