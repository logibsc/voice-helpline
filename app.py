import whisper
import sounddevice as sd
import numpy as np
import wave
import pyttsx3

model = whisper.load_model("base")
tts = pyttsx3

def record_audio(filename = "input.wav", duration = 5, samplerate = 44100):
    print("\n listening... (speak now)")
    audio_data = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype=np.int16)
    sd.wait()
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes(audio_data.tobytes())

def speak(text):
    print("responding: ", text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

while True:
    record_audio()
    result = model.transcribe("input.wav")
    user_input = result["text"].strip().lower()
    print("you said: ", user_input)

    if any(exit_word in user_input for exit_word in ["bye", "exit", "quit", "stop"]):
        speak("Goodbye, logi. Take care!")
        break

    response = f"You said: {user_input}"
    speak(response)