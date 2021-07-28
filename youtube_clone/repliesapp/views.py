from django.http import Http404
from .models import Replies
from .serializers import RepliesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.apps import apps
from django.db.models import Q

# Create your views here.


class PostReply(APIView):
    def post(self, request, comment_id):
        serializer = RepliesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class RepliesList(APIView):
    def get(self, request, comment_id):
        comment_model = apps.get_model('commentsapp.Comments')
        comment_object = comment_model.objects.get(pk=comment_id)
        replies = Replies.objects.filter(Q(comment_id=comment_id) & Q(video_id=comment_object.video_id))
        serializer = RepliesSerializer(replies, many=True)
        return Response(serializer.data)
