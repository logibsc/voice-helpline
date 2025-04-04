import speech_recognition as sr

def listen() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("waiting for your voice...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-IN')
        print("you said: ", query)
        return query
    except sr.UnknownValueError:
        print("could not understand audio.")
        return None
    except sr.RequestError as e:
        print("couldn't request results;", e)
        return None