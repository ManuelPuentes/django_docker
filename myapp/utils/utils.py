import requests

api_key = "AIzaSyBmLgPiLBJM7F01lr8X7sLbbrkXcR6u668"
video_http = "https://www.googleapis.com/youtube/v3/videos?"
channel_http = "https://www.googleapis.com/youtube/v3/channels?"
video_exist_http = "https://www.googleapis.com/youtube/v3/videos?"


def youtube_video_details(id):

    # print(id)
    
    params = {
        'key': api_key,
        'part': 'snippet',
        'id': id
    }
    response = requests.get(video_exist_http, params=params)
    data = response.json()

    return data


def get_youtube_channel_data(channel_id):

    params = {
        'key': api_key,
        'part': 'snippet',
        'id': channel_id
    }
    response = requests.get(channel_http, params=params)

    return response.json()


def fetch_youtube_popular_videos(page):

    params = {
        'key': api_key,
        'chart': 'mostPopular',
        'part': 'snippet',
        'regionCode': 'VE',
        'videoEmbeddable': True,
        'maxResults': 4 ,
    }

    if  page != 'none':
        params['pageToken'] = page


    response = requests.get(video_http, params=params)

    return response.json()


def fetch_youtube_video_data_by_id(id):
    pass
