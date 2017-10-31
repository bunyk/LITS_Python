from django.db import models

# Create your models here.

class Joke(models.Model):
    text = models.TextField()
    author = models.ForeignKey('auth.User')
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return 'Анекдот №' + str(self.id) + ' ' + self.text
