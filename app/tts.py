import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)

def speak(text: str):
    print("responding: ", text)
    engine.say(text)
    engine.runAndWait()