import re
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi, WebshareProxyConfig

def get_youtube_id(url: str) -> str:
    pattern = r"(?:v=|\/|be\/|embed\/)([a-zA-Z0-9_-]{11})"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    raise ValueError("Invalid YouTube URL")

def get_transcript(url: str) -> str:
    video_id = get_youtube_id(url)
    
    # Configure rotating proxies (replace with your proxy credentials or load from st.secrets)
    proxy_username = st.secrets.get("PROXY_USER", "")
    proxy_password = st.secrets.get("PROXY_PASS", "")

    if proxy_username and proxy_password:
        proxy_config = WebshareProxyConfig(
            username=proxy_username,
            password=proxy_password
        )
        ytt = YouTubeTranscriptApi(proxy_config=proxy_config)
    else:
        ytt = YouTubeTranscriptApi()

    transcript_list = ytt.fetch(video_id, languages=['en'])
    return " ".join([entry['text'] for entry in transcript_list])