from app.downloader import download_audio
from app.transcriber import load_whisper_model,transcribe_audio
from app.summarizer import load_summarizer,summarize_text
from app.utils import chunk_text

def run_pipeline(url):
    print("Downloading audio...")
    audio_file = download_audio(url)

    print("Loading models...")
    whisper_model = load_whisper_model()
    summarizer = load_summarizer()

    print("Transcribing...")
    text = transcribe_audio(audio_file, whisper_model)

    print("Chunking...")
    chunks = chunk_text(text)

    print("Summarizing...")
    summary = summarize_text(chunks, summarizer)

    print("\n=== FINAL SUMMARY ===\n")
    print(summary)


if __name__ == "__main__":
    youtube_url = input("Enter YouTube URL: ")
    run_pipeline(youtube_url)
