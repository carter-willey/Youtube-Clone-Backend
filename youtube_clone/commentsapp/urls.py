from django.urls import path
from . import views

urlpatterns = [
    path('videos/<str:video_id>/', views.CommentsList.as_view()),
    path('videos/<str:video_id>/post_comment', views.PostComment.as_view()),
]
