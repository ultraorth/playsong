VERSION = "1.0.0"

import json
import webbrowser
import argparse
from googleapiclient.discovery import build

with open("config.json", "r") as f:
    config = json.load(f)

API_KEY = config.get("YOUTUBE_API_KEY")
if not API_KEY:
    raise ValueError("YOUTUBE_API_KEY not found in config.json.")

def get_youtube_video_url(song_name):
    #API client
    youtube = build("youtube", "v3", developerKey=API_KEY)

    #Search for song
    request = youtube.search().list(
            q=song_name,
            part="snippet",
            type="video",
            maxResults=1
        )

    response = request.execute()

    if "items" in response and len(response["items"]) > 0:
        video_id = response["items"][0]["id"]["videoId"]
        return f"https://www.youtube.com/watch?v={video_id}"
    else:
        raise Exception("No results found for the song.")

def main():
    #parser
    parser = argparse.ArgumentParser(description="Play song on Youtube.")
    parser.add_argument("command", choices=["playsong", "play"], help="Command to execute")
    parser.add_argument("song", nargs="+", help="Name of the song to play")
    parser.add_argument("--version", action="version", version=f"playsong v{VERSION}")
    args = parser.parse_args()

    song_name = " ".join(args.song)

    try:
        video_url = get_youtube_video_url(song_name)

        print(f"Now playing: {video_url}")
        webbrowser.open(video_url)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

