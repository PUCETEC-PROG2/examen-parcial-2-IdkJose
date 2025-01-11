from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, default='Unknown')
    author = models.CharField(max_length=100, default='Unknown author')  # Agrega un valor predeterminado
    year = models.IntegerField()
    synopsis = models.TextField(default='No synopsis available')


    def __str__(self):
        return self.title


class Actor(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()

    def __str__(self):
        return self.name



