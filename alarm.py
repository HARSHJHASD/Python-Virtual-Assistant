import pyttsx3
import speech_recognition as sr 
import datetime
import os
from playsound import playsound

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

speak("At what time")
a = takeCommand()
a = a.replace(" ","")
print(a)
if len(a) == 3:
    alarm = '0' + a[0] + ":" + a[1] + a[2]
else:
    alarm = a[0] + a[1] + ":" + a[2] + a[3]

print("Anyone else?")
speak("Anything else")
choice = takeCommand()
if 'y' in choice:
    os.startfile("C:\\Users\\prakh\\source\\repos\\PythonApplication4\\PythonApplication4\\PythonApplication4.bat")
else:
    pass    
    
while(True):    
    if datetime.datetime.now().strftime("%H:%M") == alarm:
        playsound("C:\\Users\\prakh\\Downloads\\wake_up.mp3")

