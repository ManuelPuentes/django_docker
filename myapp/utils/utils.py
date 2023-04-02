import requests

api_key = "AIzaSyBmLgPiLBJM7F01lr8X7sLbbrkXcR6u668"
video_http = "https://www.googleapis.com/youtube/v3/videos?"
channel_http = "https://www.googleapis.com/youtube/v3/channels?"

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
        'regionCode': 'US',
        'maxResults': 4 ,
    }

    if  page != 'none':
        params['pageToken'] = page


    print(params)

    response = requests.get(video_http, params=params)

    return response.json()


# def request_youtube_data():



#     data = list()
#     video_data = fetch_youtube_popular_videos(api_key=api_key, url=video_http)

#     for item in video_data.get("items"):
#         snippet = item.get("snippet")
#         channel_data = get_youtube_channel_data(api_key=api_key, channel_id=snippet.get(
#             'channelId'), url=channel_http).get('items')
#         data.append({
#             "video_data": item,
#             "channel_data": channel_data[0]
#         })

#     return data