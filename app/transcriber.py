import streamlit as st
import whisper

@st.cache_resource
def load_whisper_model():
    # "tiny" or "base" uses ~150-300MB RAM compared to >1GB for larger variants
    return whisper.load_model("tiny")

def transcribe_audio(audio_path, model):
    result = model.transcribe(audio_path)
    return result["text"]