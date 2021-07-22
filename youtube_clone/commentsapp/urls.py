from django.urls import path
from . import views

urlpatterns = [
    path('videos/<str:video_id>/', views.CommentsList.as_view()),
    path('videos/post_comment/<str:video_id>/', views.PostComment.as_view()),
]
