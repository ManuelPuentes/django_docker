from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('youtube_api_v3_video_data/<str:page_token>', views.youtube_api_v3_video_data),
    path('youtube_api_v3_channel_data/<str:channel_id>', views.youtube_api_v3_channel_data),
    path('watch_video/<str:video_id>/<str:channel_name>', views.watch_video ), 

]