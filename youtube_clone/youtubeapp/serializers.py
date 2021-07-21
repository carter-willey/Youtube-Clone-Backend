from rest_framework import serializers
from .models import YoutubeVideos


class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideos
        fields = ["video_id", "likes", "dislikes", "comments"]
