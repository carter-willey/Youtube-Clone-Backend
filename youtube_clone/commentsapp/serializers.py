from rest_framework import serializers
from .models import Comments


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ["video_id", "likes", "dislikes", "comment_text"]

