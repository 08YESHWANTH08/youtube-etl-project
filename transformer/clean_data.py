import pandas as pd

def clean_data(raw_data):
    if raw_data is None:
        return pd.DataFrame()

    video_details = []
    for video in raw_data.get("items", []):
        video_details.append({
            "video_id": video["id"],
            "title": video["snippet"]["title"],
            "description": video["snippet"]["description"],
            "published_at": video["snippet"]["publishedAt"],  # Adjust the datetime format in the next step
            "channel_id": video["snippet"]["channelId"],
            "channel_title": video["snippet"]["channelTitle"],
            "views": int(video["statistics"].get("viewCount", 0)),
            "likes": int(video["statistics"].get("likeCount", 0)),
            "dislikes": int(video["statistics"].get("dislikeCount", 0))
        })

    # Convert the list of video details into a DataFrame
    return pd.DataFrame(video_details)
