import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
import os

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)

def speak(text):
    print("🔊 Speaking: ", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    mic = sr.Microphone()
    print("🎤 Waiting for your voice...")

    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("✅ Got the audio, transcribing...")

    try:
        query = r.recognize_google(audio, language='en-IN')
        print("🗣️ You said: ", query)
        return query  # ✅ RETURNING the actual query
    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"🚫 Couldn’t request results; {e}")
        return None

def generate_response(prompt):
    print("🤖 Thinking...")
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    while True:
        query = listen()
        if query:
            if query.lower() in ["stop", "exit", "quit"]:
                speak("Okay, shutting down. Bye bye!")
                break
            response = generate_response(query)
            print("💬 Gemini: ", response)
            speak(response)
