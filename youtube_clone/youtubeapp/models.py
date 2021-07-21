from django.db import models

# Create your models here.


class YoutubeVideos(models.Model):
    video_id = models.CharField(max_length=100, primary_key=True)
    likes = models.IntegerField(default=0, blank=True)
    dislikes = models.IntegerField(default=0, blank=True)
    comments = models.CharField(max_length=100, blank=True)
