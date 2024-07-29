from os import name
from django.contrib.auth.models import User
from django.db import models



class Musics(models.Model):
    
    title = models.CharField(max_length=500)
    artist = models.CharField(max_length=500)
    album = models.ForeignKey('Albums', on_delete=models.SET_NULL, null=True, blank=True)
    audio_file = models.FileField(upload_to='musics/')
    cover_image = models.ImageField(upload_to='music_image/')

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class META:
        ordering = ["title"]



class Albums(models.Model):
    name = models.CharField(max_length=400)
