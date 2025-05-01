import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# Make sure to set your OpenAI API Key
os.environ["OPENAI_API_KEY"] = "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"

# Initialize OpenAI Chat Model via LangChain
chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

def listen_to_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

def speak(text):
    print(f"Responding: {text}")
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    playsound("response.mp3")
    os.remove("response.mp3")

def chat_with_ai(prompt):
    response = chat([HumanMessage(content=prompt)])
    return response.content

def main():
    print("Voice Assistant Ready (Say 'exit' to quit)")
    while True:
        prompt = listen_to_voice()
        if prompt is None:
            continue
        if prompt.lower() == "exit":
            break
        reply = chat_with_ai(prompt)
        speak(reply)

if __name__ == "__main__":
    main()
