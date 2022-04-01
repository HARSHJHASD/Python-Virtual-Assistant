import speech_recognition as sr
from tkinter import Tk
from tkinter.filedialog import askopenfilename

import pyttsx3
import speech_recognition as sr 
import os

engine = pyttsx3.init('sapi5')
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

#print(sr.__version__)
r = sr.Recognizer()

speak("select the audio file")
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

#idx = filename.rfind('/')

#filename = str(filename[idx+1:])

file_audio = sr.AudioFile(filename)

with file_audio as source:
   audio_text = r.record(source)

f = open("Audio2txtConverted.txt",'a')
f.write(r.recognize_google(audio_text))
f.close()

print(r.recognize_google(audio_text))
print("conversion saved in txt file")
speak("conversion saved in txt file")

print("Anything else?")
speak("Anything else")
choice = takeCommand()
if 'y' in choice:
    os.startfile("C:\\Users\\prakh\\source\\repos\\PythonApplication4\\PythonApplication4\\PythonApplication4.bat")
else:
    pass  






