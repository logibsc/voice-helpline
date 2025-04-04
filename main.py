from app.stt import listen
from app.tts import speak
from app.api.gemini_api import generate_response

if __name__ == "__main__":
    while True:
        query = listen()
        if query:
            response = generate_response(query)
            speak(response)