from django.db import models

class Artist(models.Model):
    name  = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'

class Song(models.Model):
    name = models.CharField(max_length=128)
    duration = models.DurationField()
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE) # FIX ME
    album = models.ForeignKey('Album', on_delete=models.CASCADE) # FIX ME
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE) # FIX ME
    path = models.CharField(max_length=128)
    track_number = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.name}'

class Genre(models.Model):
    name = models.CharField(max_length=32)
    period = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.name}'

class Album(models.Model):
    name = models.CharField(max_length=64)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE) # FIX ME
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE) # FIX ME
    date = models.DateField()
    track_count = models.PositiveSmallIntegerField()
    front = models.BooleanField()
    cover_image = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}'
