from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import User,  Video

# from .models import Project, Task, User

# from django.contrib.auth.models import User

# from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login, authenticate
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


def auth_user(request):
    print(request.POST)

    try:
        my_user = User.objects.get(
            username=  request.POST['username'],
            password= request.POST['password']
        )

        login(request, user=my_user)
        return redirect('/')
    
    except:
         return render(request, 'login.html', { "error": "username or password incorrect "})


def create_new_user(request):

    if request.POST['password1'] == request.POST['password2']:
        try:        
            print(request.POST)
            
            new_user = User.objects.create(
                username=request.POST['username'],
                password=request.POST['password1'],
                email = request.POST['email']
            )

            id = new_user.save()

            login(request, id)

            return redirect('/')

        except IntegrityError:
            return render(request, 'signup.html', { "error": "Username already exists."})
    else:
        return render(request, 'signup.html', { "error": "Passwords did not match."})

def calculate_popularity():
    return 100

def create_new_video(request):

    print(request)

    user = User.objects.get(username='manuel')

    new_video = Video.objects.create(
        creator = user,
        title=request.POST['video_title'],
        url=request.POST['video_url'],
        likes_counter = 0,
        dislikes_counter = 0,
        popularity = calculate_popularity(),
    )

    print(request)

    id = new_video.save()
    return redirect('/')


def home(request):

    # print(request_youtube_data())
    return render(request, "index.html", {
        "youtube_data": request_youtube_data()
    })


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        return create_new_user(request=request)


def login_app(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        return auth_user(request)


def upload_video(request):
    if request.method == 'GET': 
        return render(request, 'upload_video.html')
    else:
        return create_new_video(request)


def watch_video(request, video_id, channel_name):
    return render(request, 'watch_video.html', {"video_id": video_id, "channel_name":channel_name})





