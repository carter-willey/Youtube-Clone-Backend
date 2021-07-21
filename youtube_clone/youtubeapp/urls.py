from django.urls import path
from . import views

urlpatterns = [
    path('videos/', views.VideoList.as_view()),
    path('videos/<str:pk>/', views.VideoDetail.as_view()),
]
