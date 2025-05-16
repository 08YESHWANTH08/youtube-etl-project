# extractor/fetch_youtube_data.py
import requests

def fetch_trending_videos(api_key):
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        'part': 'snippet,contentDetails,statistics',
        'chart': 'mostPopular',
        'regionCode': 'IN',
        'maxResults': 20,
        'key': api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from YouTube: {e}")
        return None
