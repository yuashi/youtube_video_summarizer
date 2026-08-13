import streamlit as st
import traceback
from app.downloader import get_transcript
from app.utils import chunk_text
from app.summarizer import load_summarizer, summarize_text

st.set_page_config(page_title="YouTube Summarizer", layout="wide")
st.title("🎥 YouTube Video Summarizer")

url = st.text_input("Enter YouTube URL")

if st.button("Generate Summary"):
    if url:
        try:
            with st.spinner("Fetching transcript..."):
                text = get_transcript(url)

            with st.spinner("Loading summarizer..."):
                summarizer = load_summarizer()

            with st.spinner("Chunking text..."):
                chunks = chunk_text(text)

            with st.spinner("Summarizing..."):
                summary = summarize_text(chunks, summarizer)

            st.success("Done!")
            st.subheader("📄 Summary")
            st.write(summary)

        except Exception as e:
            st.error(f"Error: {e}")
            st.code(traceback.format_exc())
    else:
        st.warning("Please enter a URL")