from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
# from .models import User,  Video
from .models import Video

# from .models import Project, Task, User

from django.contrib.auth.models import User

# from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


import requests


# Create your views here.

def get_channel_icon(api_key, channel_id, url):

    params = {
        'key': api_key,
        'part': 'snippet',
        'id': channel_id
    }
    response = requests.get(url, params=params)

    return response.json()


def fetch_youtube_popular_videos(api_key, url):

    params = {
        'key': api_key,
        'chart': 'mostPopular',
        'part': 'snippet',
        'regionCode': 'US',
        'maxResults': 15
    }
    response = requests.get(url, params=params)

    return response.json()


def request_youtube_data():

    api_key = "AIzaSyBmLgPiLBJM7F01lr8X7sLbbrkXcR6u668"
    video_http = "https://www.googleapis.com/youtube/v3/videos?"
    channel_http = "https://www.googleapis.com/youtube/v3/channels?"

    data = list()
    video_data = fetch_youtube_popular_videos(api_key=api_key, url=video_http)

    for item in video_data.get("items"):
        snippet = item.get("snippet")
        channel_data = get_channel_icon(api_key=api_key, channel_id=snippet.get(
            'channelId'), url=channel_http).get('items')
        data.append({
            "video_data": item,
            "channel_data": channel_data[0]
        })

    return data


def home(request):

    # print(request_youtube_data())
    return render(request, "index.html", {
        "youtube_data": request_youtube_data()
    })


def signup_method(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        return create_new_user(request=request)


def create_new_user(request):

    if request.POST['password1'] == request.POST['password2']:
        try:
            print(request.POST)
            new_user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
            )
            new_user.save()
            login(request, new_user)
            return redirect('/')

        except IntegrityError:
            return render(request, 'signup.html', {"error": "Username already exists."})
    else:
        return render(request, 'signup.html', {"error": "Passwords did not match."})


def login_method(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        try:
            user = authenticate(
                request, username=request.POST['username'], password=request.POST['password'])
            login(request, user)
            return redirect('/')
        except:
            return render(request, 'login.html', {"error": "Username or password is incorrect."})


def upload_video(request):
    if request.method == 'GET':
        return render(request, 'upload_video.html')
    else:
        return create_new_video(request)


def create_new_video(request):

    print(request.POST)

    if request.user.is_authenticated:
        new_video = Video.objects.create(
            creator=request.user.username,
            title=request.POST['video_title'],
            url=request.POST['video_url'],
            likes_counter=0,
            dislikes_counter=0,
            popularity=calculate_popularity(),
        )
        new_video.save()

        return redirect('/')
    else:
        return redirect('/')


                 

def calculate_popularity():
    return 100



def watch_video(request, video_id, channel_name):
    return render(request, 'watch_video.html', {"video_id": video_id, "channel_name": channel_name})










