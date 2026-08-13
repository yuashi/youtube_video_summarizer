import re
from youtube_transcript_api import YouTubeTranscriptApi

def get_youtube_id(url: str) -> str:
    """Extract 11-character video ID from various YouTube URL formats."""
    pattern = r"(?:v=|\/|be\/|embed\/)([a-zA-Z0-9_-]{11})"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    raise ValueError("Invalid YouTube URL")

def get_transcript(url: str) -> str:
    """Fetch official or auto-generated captions from YouTube."""
    video_id = get_youtube_id(url)
    
    # Instantiate API client
    ytt = YouTubeTranscriptApi()
    
    # Try fetching English captions (or fell back to auto-generated)
    transcript_list = ytt.fetch(video_id, languages=['en'])
    
    # Combine individual caption snippets into continuous text
    full_text = " ".join([entry['text'] for entry in transcript_list])
    return full_text