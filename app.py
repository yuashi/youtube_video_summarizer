import streamlit as st
import os
import traceback
from app.downloader import download_audio
from app.utils import chunk_text
from app.transcriber import load_whisper_model, transcribe_audio
from app.summarizer import load_summarizer, summarize_text

st.set_page_config(page_title="YouTube Summarizer", layout="wide")

st.title("🎥 YouTube Video Summarizer")

url = st.text_input("Enter YouTube URL")

if st.button("Generate Summary"):
    if url:
        audio_file = None
        try:
            with st.spinner("Loading models..."):
                whisper_model = load_whisper_model()
                summarizer = load_summarizer()

            with st.spinner("Downloading audio..."):
                audio_file = download_audio(url)

            with st.spinner("Transcribing..."):
                text = transcribe_audio(audio_file, whisper_model)

            with st.spinner("Chunking text..."):
                chunks = chunk_text(text)

            with st.spinner("Summarizing..."):
                summary = summarize_text(chunks, summarizer)

            st.success("Done!")

            st.subheader("📄 Summary")
            st.write(summary)
            
        except Exception as e:
            st.error(f"Error: {e}")
            st.code(traceback.format_exc())  # Prints full stack trace for easy copy-pasting
            
        finally:
            if audio_file and os.path.exists(audio_file):
                os.remove(audio_file)

    else:
        st.warning("Please enter a URL")