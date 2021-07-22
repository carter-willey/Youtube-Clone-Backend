from rest_framework import serializers
from .models import Replies


class RepliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Replies
        fields = ["comment_id", "video_id", "likes", "dislikes", "comment_text"]

