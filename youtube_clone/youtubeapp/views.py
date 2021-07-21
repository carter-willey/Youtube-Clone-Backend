from django.http import Http404
from .models import YoutubeVideos
from .serializers import YoutubeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class VideoList(APIView):

    def get(self, request):
        youtube_videos = YoutubeVideos.objects.all()
        serializer = YoutubeSerializer(youtube_videos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = YoutubeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VideoDetail(APIView):

    def get_object(self, pk):
        try:
            return YoutubeVideos.objects.get(pk=pk)
        except YoutubeVideos.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        video = self.get_object(pk)
        serializer = YoutubeSerializer(video)
        return Response(serializer.data)

    def put(self, request, pk):
        video = self.get_object(pk)
        """
        if song.do_you_like_the_song:
            song.likes = 1 + int(song.likes)
        """
        serializer = YoutubeSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        video = self.get_object(pk)
        serializer = YoutubeSerializer(video)
        video.delete()
        return Response(serializer.data)
