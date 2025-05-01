# Voice LangChain Assistant

A voice-enabled assistant using LangChain, OpenAI, Speech-to-Text, and Text-to-Speech. It captures voice input, generates AI responses, and speaks them out loud.
This project uses voice input to interact with an AI model via LangChain and OpenAI. The assistant:

- Captures speech through a microphone.
- Transcribes it using Google STT (or Whisper optionally).
- Sends the text to OpenAI's GPT-3.5 via LangChain.
- Reads out the response using Google Text-to-Speech (gTTS).

## Installation

```bash
pip install -r requirements.txt

