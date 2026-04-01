#ai.py -Handle the main logic for Mothusi, including interactions with Google GenAI and coordinating the listen and speak features
import os

from groq import Groq #to allow mothusi to use google genai to answer questions and have conversations with me
from features.speak import engine #to allow mothusi to speak the answers from google genai
from dotenv import load_dotenv #to allow mothusi to load the API key for google genai from the .env file
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY")) #to allow mothusi to use google genai to answer questions and have conversations with me

def ask(question):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are Mothusi. Give answers in 2 sentences or less"},
                {"role": "user", "content": question}
            ]
        )
        answer = response.choices[0].message.content
        print("Mothusi says: " + answer)
        import subprocess
        clean_answer = answer.replace("'", "").replace('"', '')  # Escape single and double quotes for PowerShell
        subprocess.call(["powershell", "-Command", f"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{clean_answer}');"])
    except Exception as e:
        print("An error occurred while trying to get a response from Google GenAI: " + str(e))
    
