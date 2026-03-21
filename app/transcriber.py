import whisper
import torch
import streamlit as st

# print(torch.__version__)
# print(torch.cuda.is_available())
# print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU")

@st.cache_resource
def load_whisper_model(model_size="base"):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = whisper.load_model(model_size).to(device)
    return model


def transcribe_audio(file_path,model):
    result = model.transcribe(file_path,task="translate")
    return result["text"]