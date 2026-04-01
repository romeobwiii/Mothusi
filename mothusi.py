#Mothusi -Student Voice Assistant - A voice assistant designed to help students with their studies, using Google GenAI for answering questions and providing information, as well as handling various commands and interactions.
#Built with Python, utilizing libraries such as pyttsx3 for text-to-speech, speech_recognition for speech recognition, and the Groq client for interacting with Google GenAI.
#By Mulax Prime - Gaborone , Botswana
#Version 1.0 - Initial release

import time #to allow mothusi to handle timing and delays
from features.speak import speak #to allow mothusi to speak
from features.listen import listen #to allow mothusi to listen and understand what you say
from features.commands import open_word, open_powerpoint, goodbye #to allow mothusi to execute commands like opening Microsoft Word and PowerPoint, and saying goodbye
from features.ai import ask #to allow mothusi to use google genai to answer questions and have conversations with me

def greet():
    speak("Hello! I am Mothusi, your personal assistant. How can I help you today?")

greet()
time.sleep(4) #to allow mothusi to pause for a moment before listening for commands

running = True
while running:
     command = listen()
     if command:
        if "exit" in command or "goodbye" in command:
            goodbye()
            running = False
        elif "open word" in command:
            open_word()
        elif "open powerpoint" in command:
            open_powerpoint()
        else:
            time.sleep(1) #to allow mothusi to pause briefly before responding to the command
            ask(command)
