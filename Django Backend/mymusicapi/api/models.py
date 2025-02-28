from django.db import models

class Song(models.Model):
    song_title = models.CharField(max_length=255)
    song_artist = models.CharField(max_length=255)
    song_image = models.ImageField(upload_to='images/', blank=True, null=True)  # Stores in media/images/
    song_audio = models.FileField(upload_to='audio/', blank=True, null=True)   # Stores in media/audio/

    def __str__(self):
        return self.song_title
