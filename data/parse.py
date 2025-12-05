import os
from dotenv import load_dotenv
from googleapiclient.discovery import build


load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found")

youtube = build("youtube", "v3", developerKey=API_KEY)

def get_channel_id(channel_name):
    res = youtube.search().list(
        q=channel_name,
        part="snippet",
        type="channel",
        maxResults=1
    ).execute()

    return res["items"][0]["snippet"]["channelId"]


def get_uploads_playlist(channel_id):
    res = youtube.channels().list(
        part="contentDetails",
        id=channel_id
    ).execute()

    return res["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]


def get_videos_with_keywords(playlist_id, keywords):
    matched_ids = []
    next_page = None

    while True:
        res = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page
        ).execute()

        for item in res["items"]:
            title = item["snippet"]["title"].lower()
            video_id = item["snippet"]["resourceId"]["videoId"]

            if any(word.lower() in title for word in keywords):
                matched_ids.append(video_id)

        next_page = res.get("nextPageToken")
        if not next_page:
            break

    return matched_ids

channel_name = "CNN"
keywords = ["Ukraine", "Russia", "Putin", "Zelenskiy", "ukrainain", "russian", "kyiv", "mariupol", "kherson", "western ukraine", "kharkiv", "donbass"]

print(f"🔍 Searching channel: {channel_name}")

channel_id = get_channel_id(channel_name)
playlist_id = get_uploads_playlist(channel_id)
result = get_videos_with_keywords(playlist_id, keywords)


output_file = "video_ids.txt"

with open(output_file, "w") as f:
    for vid in result:
        f.write(vid + "\n")

print(f"✅ Done! Found {len(result)} videos.")
print(f"💾 Saved to {output_file}")
