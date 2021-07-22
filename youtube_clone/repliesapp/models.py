from django.db import models

# Create your models here.


class Replies(models.Model):
    comment = models.ForeignKey('commentsapp.Comments', on_delete=models.CASCADE)
    video_id = models.CharField(max_length=100)
    likes = models.IntegerField(default=0, blank=True)
    dislikes = models.IntegerField(default=0, blank=True)
    comment_text = models.CharField(max_length=100, blank=True)
