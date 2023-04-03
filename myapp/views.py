from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .utils.utils import fetch_youtube_popular_videos, get_youtube_channel_data, youtube_video_details

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

from .models import Video
from .forms import UploadVideoForm


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
    return render(request, 'watch_video.html', {"video_id": video_id, "channel_name": channel_name})


class user_signup(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "create_user.html", {"form": form})

    def post(self, request):

        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "create_user.html", {"form": form})


class user_authenticate(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "authenticate.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password")
            )
            if user is not None:
                login(request, user)
                return redirect('home')

        return render(request, "authenticate.html", {"form": form})


class upload_video(View):
    def get(self, request):
        form = UploadVideoForm()
        return render(request, "upload_video.html", {"form": form})

    def post(self, request):
        form = UploadVideoForm()
        new_video = Video.objects.create(
            src=request.POST.get('src'),
            title=request.POST.get('title'),
            creator=request.user,
            thumbnail=request.POST.get('thumbnail'),
        )
        new_video.save()
        # should redirect to user uploaded videos panel in the future
        return redirect('home')



def user_logout(request):
    logout(request)
    return redirect('home')


@csrf_exempt
def comment_video(request, title):

    # in my app there arre two cases,
    # 1 user already created this video ,
    # 2 the video was fetched from youtube api and we should created
    video_exist = False

    try:
        video = Video.objects.get(src=title)
        video_exist = True
    except:
        youtube_data = youtube_video_details(title)
        page_info = youtube_data.get("pageInfo")
        if (page_info.get("totalResults")):

            new_video = create_video_instance_from_youtube_data(
                (youtube_data.get("items"))[0])
            new_video.save()
            video_exist = True
        else:
            return HttpResponse('no existe este video')

    if video_exist:
        print("el video existe")
        return HttpResponse('video existe')

    # return HttpResponse('ok')

    # if request.user.is_authenticated:

    #     new_video =  Video.objects.create(
    #         creator=request.user,
    #         title=video_id
    #     )

    #     new_video.save()
    #     return HttpResponse('estas auth')

    # else:
    #     return HttpResponse('no estas auth')


def create_video_instance_from_youtube_data(data):

    snippet = data.get("snippet")
    thumbnails = snippet.get('thumbnails')

    video_id = data.get('id')
    video_title = snippet.get('title')
    video_channel = snippet.get('channelTitle')
    thumbnail = (thumbnails.get('standard')).get("url")

    return Video.objects.create(
        src=video_id,
        title=video_title,
        creator=video_channel,
        thumbnail=thumbnail,
    )
