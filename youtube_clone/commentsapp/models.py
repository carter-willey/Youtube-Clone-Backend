from django.db import models

# Create your models here.


class Comments(models.Model):
    video_id = models.CharField(max_length=100)
    likes = models.IntegerField(default=0, blank=True)
    dislikes = models.IntegerField(default=0, blank=True)
    comment_text = models.CharField(max_length=100, blank=True)

