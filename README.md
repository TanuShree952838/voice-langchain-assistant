# Voice LangChain Assistant

A voice-enabled assistant using LangChain, OpenAI, Speech-to-Text, and Text-to-Speech. It captures voice input, generates AI responses, and speaks them out loud.

This project uses voice input to interact with an AI model via LangChain and OpenAI. The assistant:

- Captures speech through a microphone.
- Transcribes it using Google STT (or Whisper optionally).
- Sends the text to OpenAI's GPT-3.5 via LangChain.
- Reads out the response using Google Text-to-Speech (gTTS).

---

# Colab Voice Assistant AI

This notebook enables a voice assistant inside Google Colab that:

- Uses your browser's mic to record audio
- Converts speech to text using Google Speech Recognition
- Generates responses using HuggingFace's FLAN-T5 small model
- Responds back using Google Text-to-Speech (gTTS)

## Getting Started in Colab

1. Run all cells in `voice_assistant_colab.ipynb`.
2. Record your voice using the browser-based mic recorder.
3. It will transcribe your audio, run it through the AI model, and speak the result.

## Requirements

Install packages in Colab:

```python
!pip install transformers torch speechrecognition pydub gtts ipython
!apt install ffmpeg  # Required for audio processing
```
