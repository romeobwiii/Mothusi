#speak.py - Handle text-to-speech and speech recognition for Mothusi
import pyttsx3 #to allow mothusi to speak

engine = pyttsx3.init()
voices = engine.getProperty('voices')
if voices:
    selected_voice = voices[1].id if len(voices) > 1 else voices[0].id
    engine.setProperty('voice', selected_voice)
engine.setProperty('rate', 150)  # Adjust the speech rate (default is usually 200)

def speak(text):
    engine.say(text)
    engine.runAndWait()