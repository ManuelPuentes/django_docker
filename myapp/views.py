from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied

from .utils.utils import fetch_youtube_popular_videos, get_youtube_channel_data


def home(request):
    return render(request, "index.html")


def youtube_api_v3_video_data(request, page_token):
    if request.method == 'GET':
        return JsonResponse(fetch_youtube_popular_videos(page_token))
    else:
        raise PermissionDenied("only read requests")

def youtube_api_v3_channel_data(request, channel_id):
    if request.method == 'GET':
        return JsonResponse(get_youtube_channel_data(channel_id), safe=False)
    else:
        raise PermissionDenied("only read requests")
    

def watch_video(request, video_id, channel_name):
    return render(request, 'watch_video.html',{"video_id": video_id, "channel_name": channel_name})











