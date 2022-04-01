from moviepy.editor import *
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

speak("Please select the video file to be converted")
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

'''video_exts = r"*.mp4"  
filename = askopenfilename(
                                              title="Select a File",
                                              filetypes=(("video files",
                                                          video_exts)))
'''

speak("converting")
mp4_file = filename
mp3_file = 'mp4TOmp3Converted.mp3'
videoclip = VideoFileClip(mp4_file)
audioclip = videoclip.audio
audioclip.write_audiofile(mp3_file)
speak("File Converted")
print("File Converted")
audioclip.close()
videoclip.close()

print("Anything else?")
speak("Anything else")
choice = takeCommand()
if 'y' in choice:
    os.startfile("C:\\Users\\prakh\\source\\repos\\PythonApplication4\\PythonApplication4\\PythonApplication4.bat")
else:
    pass                           
