from django.urls import path
from . import views

urlpatterns = [
    #path('/', views.video_list, name='video_list'),
    path('video_list/', views.video_list, name='video_list'),
    path('video_list/dash/', views.dash, name='dash'),
    path('video_list/hls/', views.hls, name='hls'),
    path('video_list/upload/', views.upload, name='upload'),
    path('video_list/video_hls/<str:video_title>/', views.video_hls, name='video_hls'),
    path('video_list/video_dash/<str:video_title>/', views.video_dash, name='video_dash'),
]

