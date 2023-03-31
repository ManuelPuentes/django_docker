from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login_app, name='login'),
    path('upload_video', views.upload_video, name='upload_video'),
    path('watch_video/<str:video_id>/<str:channel_name>', views.watch_video ), 
]