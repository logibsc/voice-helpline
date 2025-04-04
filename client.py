import requests
import speech_recognition as sr

# 🔹 Ngrok URL (Replace with the one from Colab)
FAISS_SERVER_URL = "https://70eb-34-125-235-37.ngrok-free.app"

# 🔹 Initialize Speech Recognition
recognizer = sr.Recognizer()

def recognize_speech():
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print(f"📝 Recognized: {text}")
            return text
        except sr.UnknownValueError:
            print("❌ Could not understand the audio.")
        except sr.RequestError:
            print("❌ Could not request results from Google Speech Recognition.")

    return None

def search_faiss(query_text):
    response = requests.post(f"{FAISS_SERVER_URL}/search", json={"text": query_text})
    if response.status_code == 200:
        print("✅ FAISS Search Results:", response.json()["results"])
    else:
        print("❌ Error:", response.text)

if __name__ == "__main__":
    spoken_text = recognize_speech()
    if spoken_text:
        search_faiss(spoken_text)
