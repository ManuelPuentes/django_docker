from django.urls import path
from . import views 




urlpatterns = [
    path('', views.home, name='home'),
    path('youtube_api_v3_video_data/<str:page_token>', views.youtube_api_v3_video_data),
    path('youtube_api_v3_channel_data/<str:channel_id>', views.youtube_api_v3_channel_data),
    path('watch_video/<str:video_id>/<str:channel_name>', views.watch_video), 
    path('signup/', views.user_signup.as_view(), name='signup'),
    path('login/', views.user_authenticate.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('upload_video/', views.upload_video.as_view(), name='upload_video'),
    path('comment_video/<str:title>', views.comment_video, name = 'comment_video')
]