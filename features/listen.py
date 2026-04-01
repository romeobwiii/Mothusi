#listen.py Handels all the voice input for Mothusi 
import speech_recognition as sr
from features.speak import speak

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You said: " + command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry.")
        return ""
    except sr.RequestError as e:
        print(f"No internet connection: {e}")
        return ""