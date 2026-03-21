# 🎥 YouTube Video Summarizer

An end-to-end AI application that summarizes YouTube videos using **speech recognition and natural language processing**.
Instead of relying on existing transcripts, this project converts audio → text → summary using deep learning models.

---

## 🚀 Features

- 🎧 Download audio directly from YouTube
- 🗣️ Speech-to-text using Whisper (multi-language support)
- 🌍 Automatic translation to English
- 🧠 Text summarization using transformer models (BART)
- ⚡ GPU acceleration (if available)
- 🖥️ Interactive web UI built with Streamlit
- 🧹 Automatic cleanup of temporary audio files

---

## 🧠 How It Works

```text
YouTube URL
   ↓
Audio Download (yt-dlp)
   ↓
Speech-to-Text (Whisper)
   ↓
Text Chunking
   ↓
Summarization (BART Transformer Model)
   ↓
Final Summary
```

---

## 🛠️ Tech Stack

- Python 3.10
- Whisper (Speech Recognition)
- Hugging Face Transformers (BART)
- PyTorch (GPU support)
- Streamlit (UI)
- yt-dlp (YouTube audio extraction)
- FFmpeg

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yuashi/youtube_video_summarizer.git
cd youtube_video_summarizer
```

---

### 2. Create virtual environment (Python 3.10 recommended)

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 4. Install FFmpeg

Required for audio processing:

- Windows: Download from https://ffmpeg.org and add to PATH
- Mac: `brew install ffmpeg`
- Linux: `sudo apt install ffmpeg`

---

### 5. (Optional) Enable GPU

Install CUDA-enabled PyTorch:

```bash
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu126
```

---

## ▶️ Usage

### Run the Streamlit app

```bash
streamlit run app.py
```

Then:

1. Paste a YouTube URL
2. Click **Generate Summary**
3. View the AI-generated summary

---

## 🌍 Multilingual Support

- Automatically detects spoken language
- Can translate speech → English before summarization
- Works with Hindi, Spanish, German, etc.

---

## ⚡ Performance Notes

- GPU significantly speeds up transcription and summarization
- Whisper model size affects speed vs accuracy:
  - `tiny` → fastest
  - `base` → balanced (recommended)
  - `small+` → more accurate, slower

---

## 🧩 Project Structure

```text
youtube_video_summarizer/
│
├── app/
│   ├── downloader.py
│   ├── transcriber.py
│   ├── summarizer.py
│   ├── utils.py
│   └── __init__.py
│
├── app.py              # Streamlit UI
├── main.py             # CLI entry point
├── requirements.txt
└── README.md
```

---

## 🔮 Future Improvements

- 📊 Bullet-point & structured summaries
- 🎬 Video preview (thumbnail + metadata)
- ⏱️ Timestamp-based summaries
- 💾 Export summary as PDF
- 🌐 Deploy to cloud (Streamlit Cloud / AWS)
- 🧠 Use advanced LLMs for better summaries

---

## ⚠️ Limitations

- Long videos may take time to process
- Accuracy depends on audio quality
- Summarization model works best with English text

---

## 📄 License

MIT License

---

## ⭐ Acknowledgements

- OpenAI Whisper for speech recognition
- Meta BART for transformer model
- Streamlit for rapid UI development

---

## 🙌 Author

GitHub: https://github.com/yuashi
