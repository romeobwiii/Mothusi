#commands.py -Define the commands that Mothusi can understand and execute
import os #to allow mothusi to interact with the operating system
import subprocess #to allow mothusi to run system commands
from features.speak import speak #to allow mothusi to speak

def open_word():
    speak("Opening Microsoft Word...")
    os.startfile("winword.exe")

def open_powerpoint():
    speak("Opening Microsoft PowerPoint...")
    os.startfile("powerpnt.exe")

    
def goodbye():
    subprocess.call(['powershell', '-Command', 'Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak("Goodbye. Study hard.")'])
    raise SystemExit
