import re
import requests

def get_youtube_id(url: str) -> str:
    pattern = r"(?:v=|\/|be\/|embed\/)([a-zA-Z0-9_-]{11})"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    raise ValueError("Invalid YouTube URL")

def get_transcript(url: str) -> str:
    video_id = get_youtube_id(url)
    
    # Use Invidious public API to pull captions without IP bans
    invidious_instances = [
        "https://inv.riverside.rocks",
        "https://invidious.nerdvpn.de",
        "https://yt.artemislena.eu"
    ]
    
    for instance in invidious_instances:
        try:
            res = requests.get(f"{instance}/api/v1/captions/{video_id}", timeout=5)
            if res.status_code == 200:
                captions = res.json().get("captions", [])
                if captions:
                    # Fetch first English caption track
                    caption_url = f"{instance}{captions[0]['url']}"
                    caption_res = requests.get(caption_url, timeout=5)
                    # Simple text extraction from webvtt / srt output
                    clean_text = " ".join(
                        line for line in caption_res.text.splitlines() 
                        if not line.startswith("WEBVTT") and not "-->" and line.strip()
                    )
                    if clean_text:
                        return clean_text
        except Exception:
            continue

    raise Exception("Could not fetch transcript from public nodes. Try another video.")