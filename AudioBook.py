from gtts import gTTS
import tkinter as tk
from tkinter import simpledialog
import os
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
#engine = pyttsx3.init('dummy')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        r.energy_threshold = 4000
        print("Listening...") 
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        query = takeCommand()

    return query


ROOT = tk.Tk()
ROOT.withdraw()
speak("Enter the text to be converted as Audio Book")
TEXT = simpledialog.askstring(title="TEXT2AUDIO", prompt="Enter the text")


tts = gTTS(TEXT, lang='en')
tts.save('AudioBook.mp3')

speak("Audio Book created")
print("AudioBook created")

print("Anything else?")
speak("Anything else")
choice = takeCommand()
if 'y' in choice:
    os.startfile("C:\\Users\\prakh\\source\\repos\\PythonApplication4\\PythonApplication4\\PythonApplication4.bat")
else:
    pass  
