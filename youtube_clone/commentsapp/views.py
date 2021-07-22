from django.http import Http404
from .models import Comments
from .serializers import CommentsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class PostComment(APIView):

    def post(self, request):
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentsList(APIView):

    def get(self, request, video_id):
        comments = Comments.objects.filter(video_id=video_id)
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        video = self.get_object(pk)
        """
        if song.do_you_like_the_song:
            song.likes = 1 + int(song.likes)
        """
        serializer = CommentsSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        video = self.get_object(pk)
        serializer = CommentsSerializer(video)
        video.delete()
        return Response(serializer.data)
