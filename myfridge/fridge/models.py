from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Recipy(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True, editable=False)
    author = models.ForeignKey('auth.User')
    recipy = models.ForeignKey(Recipy)
    likes_count = models.IntegerField()


class Ingredient(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    recipy = models.ForeignKey(Recipy, on_delete=models.CASCADE)
    amount = models.FloatField()

    def __str__(self):
        return self.product.name + ' -> ' + self.recipy.name
