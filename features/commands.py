import os
import subprocess
from features.speak import speak
from docx import Document
from features.listen import listen

def ps_speak(text):
    subprocess.call(['powershell', '-Command', 
        f'Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak("{text}")'])

def open_word():
    speak("Opening Microsoft Word...")
    os.startfile("winword.exe")

def open_powerpoint():
    speak("Opening Microsoft PowerPoint...")
    os.startfile("powerpnt.exe")

def record_this():
    ps_speak("Ready. Go ahead.")
    notes = []
    while True:
        command = listen()
        if not command:
            continue
        if "stop" in command or "record off" in command:
            break
        else:
            notes.append(command)
    doc = Document()
    for note in notes:
        doc.add_paragraph(note)
    ps_speak("Done. I have your notes.")
    doc.save("Mothusi_notes.docx")
    os.startfile("Mothusi_notes.docx")

def goodbye():
    subprocess.call(['powershell', '-Command', 
        'Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak("Goodbye. Study hard.")'])
    raise SystemExit
