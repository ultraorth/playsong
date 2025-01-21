VERSION = "1.0.1"
import requests
import json
import webbrowser
import argparse
from googleapiclient.discovery import build
import os
import sys
import shutil


app_dir = os.path.dirname(sys.executable)

config_path = os.path.join(app_dir, "config.json")

try:
    with open(config_path, "r") as f:
        config = json.load(f)
except FileNotFoundError:
    print(f"Error: config.json not found in {app_dir}.")
    print("Please make sure the config.json file is in the same directory as the executable.")
    sys.exit(1)

API_KEY = config.get("YOUTUBE_API_KEY")
if not API_KEY:
    raise ValueError("YOUTUBE_API_KEY not found in config.json.")

def check_for_update(current_version):
    repo_url = "https://api.github.com/repos/ultraorth/playsong/releases/latest"
    try:
        response = requests.get(repo_url)
        response.raise_for_status()
        latest_release = response.json()
        latest_version = latest_release["tag_name"]

        if latest_version != current_version:
            print(f"A new version {latest_version} is available!")
            print(f"Download it from: {latest_release['html_url']}")
            
        else:
            print("You are using the latest version.")
    except Exception as e:
        print(f"Failed to check for updates: {e}")

def upgrade_app(current_version):
    repo_url = "https://api.github.com/repos/ultraorth/playsong/releases/latest"
    
    try:
        #get latest release info
        response = requests.get(repo_url)
        response.raise_for_status()
        latest_release = response.json()
        latest_version = latest_release["tag_name"]

        if latest_version == current_version:
            print("You are using the latest version.")
            return
        
        print(f"A new version {latest_version} is available!")
        print("Downloading the update...")

        #find the download url for the executable
        assets = latest_release.get("assets", [])
        if not assets:
            print("No executable found in the release.")
            return

        download_url = assets[0]["browser_download_url"]

        response = requests.get(download_url, stream=True)
        response.raise_for_status()

        #save executable
        temp_file = "playsong_new"
        with open(temp_file, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
            
        #replace old executable
        if os.name == "nt":
            os.replace(temp_file, "playsong.exe")
        else:
            os.replace(temp_file, "playsong")
            os.chmod("playsong", 0o755)
        
        print("Update complete! Please restart the app.")
        sys.exit()

    except Exception as e:
        print(f"Failed to upgrade: {e}")

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
    '''
    parser.add_argument("command", nargs="?", choices=["playsong", "play"], help="Command to execute")
    '''
    parser.add_argument("song", nargs="*", help="Name of the song to play")
    parser.add_argument("--version", action="version", version=f"playsong v{VERSION}")
    parser.add_argument("--check-update", action="store_true", help="Check for updates")
    parser.add_argument("--upgrade", action="store_true", help="Upgrade to the latest version.")
    args = parser.parse_args()

    if args.check_update:
        check_for_update(VERSION)
        return
    if args.upgrade:
        upgrade_app(VERSION)
        return
    
    if not args.song:
        parser.print_help()
        return
    
    song_name = " ".join(args.song)

    try:
        video_url = get_youtube_video_url(song_name)

        print(f"Now playing: {video_url}")
        webbrowser.open(video_url)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

