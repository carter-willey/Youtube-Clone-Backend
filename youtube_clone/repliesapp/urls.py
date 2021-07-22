from django.urls import path
from . import views

app_name = "replies"
urlpatterns = [
    path('videos/reply/<int:comment_id>/', views.RepliesList.as_view()),
    path('videos/post_reply/<int:comment_id>/', views.PostReply.as_view()),
]
