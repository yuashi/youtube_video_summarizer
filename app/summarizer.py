from transformers import pipeline
import torch
import streamlit as st


@st.cache_resource
def load_summarizer():
    device = 0 if torch.cuda.is_available() else -1

    summarizer = pipeline(
        "summarization",
        model="facebook/bart-large-cnn",
        device=device
    )
    return summarizer


def summarize_text(text_chunks,summarizer):
    summaries = []

    for chunk in text_chunks:
        summary = summarizer(chunk, max_length=120, min_length=30, do_sample=False)
        summaries.append(summary[0]['summary_text'])

    return " ".join(summaries)