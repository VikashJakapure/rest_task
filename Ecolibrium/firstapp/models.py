from __future__ import unicode_literals
from django.conf import settings
from django.db import models

class Profiles(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class Genre(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name


class Movie(models.Model):
    popularity = models.FloatField()
    director = models.CharField(max_length=500)
    genre = models.ManyToManyField(Genre,related_name="genre")
    imdb_score = models.FloatField()
    name = models.CharField(max_length=500)
    class Meta:
        ordering = ('-imdb_score',)

    def __str__(self):
        return self.name