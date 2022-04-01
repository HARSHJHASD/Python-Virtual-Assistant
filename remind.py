import pyttsx3
import speech_recognition as sr 
import datetime
import os
from playsound import playsound

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

print("What do you want me to remind")
speak("What do you want me to remind")
remind = takeCommand()
print("DATE")
speak("date")
reminddate = takeCommand().split()
print("And TIME")
speak("And Time")
remindtime = takeCommand()
remindtime = remindtime.replace(" ", "")            
a = remindtime
if len(a) == 3:
    remindtime = '0' + a[0] + ":" + a[1] + a[2]
else:
    remindtime = a[0] + a[1] + ":" + a[2] + a[3]
            
x = datetime.datetime.now()
sysdate = x.day
sysmonth = x.strftime("%B")
print("Reminder set for", reminddate[0], reminddate[1], "at ", remindtime, "hours")
speak(f"Reminder set for: {reminddate[0]} {reminddate[1]} at {remindtime} hours")

print("Anything else?")
speak("Anything else")
choice = takeCommand()
if 'y' in choice:
    os.startfile("C:\\Users\\prakh\\source\\repos\\PythonApplication4\\PythonApplication4\\PythonApplication4.bat")
else:
    pass  

while(True):
    if str(sysdate) == str(reminddate[0]) and str(sysmonth) == str(reminddate[1]) and str(datetime.datetime.now().strftime("%H:%M")) == str(remindtime): 
        print("REMINDER")
        playsound("C:\\Users\\prakh\\Downloads\\Reminder.mp3") 
