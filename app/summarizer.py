import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_summarizer():
    return pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6"
    )

def summarize_text(chunks, summarizer):
    summaries = []
    for chunk in chunks:
        # Generate summary per text chunk
        res = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        summaries.append(res[0]['summary_text'])
    return " ".join(summaries)