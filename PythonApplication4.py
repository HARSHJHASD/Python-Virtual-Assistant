import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition 
import datetime
import wikipedia #pip install wikipedia

import webbrowser
import os
from playsound import playsound
import sys
import time
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import pyautogui

#os.environ["PYDEVD_USE_FRAME_EVAL"] = "NO" //to sollve some frame eval error while voice recog.

#engine = pyttsx3.init('dummy')
engine = pyttsx3.init('sapi5') #pythoncom error, installed pywin32
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    global a
    a = 0
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Corona Sir. Harsh please tell me how may I help you")       
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer() 
    with sr.Microphone() as source: #req pyaudio that's not for py3.7 and above.. therefore first install pipwin and then pipwin install pyaudio, pyaudio actually helps in using c module portaudio
        r.energy_threshold = 1000  #default value is  4000 #higher it is, lower the sesntivity and better for noisy environment
        print("Listening...") 
        r.pause_threshold = 1 #pause after which voice-input will be considered over
        audio = r.listen(source)
        
        #print(audio)
        #temp = r.listen(source)
        #print(str(temp))
        print("listened")
        

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        query = takeCommand()
    
    return query

if __name__ == "__main__":
#if __name__ == "__main__":
    wishMe()
    def mains():
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:   #tell me about someone from wikipedia
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()
            

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()
            

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()

        elif 'music' in query:
            #music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            #songs = os.listdir(music_dir)
            #print(songs)    
            #os.startfile(os.path.join(music_dir, songs[0]))
            webbrowser.open("google.com/music")
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()
            
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()

        elif 'witter' in query: #via playstore of window
            #os.startfile("C:\\Users\\prakh\\source\\repos\\PythonApplication4\\PythonApplication4\\twitter.bat")
            os.system('cmd /k "explorer.exe shell:appsFolder\9E2F88E3.Twitter_wgeqdkkx372wm!Twitter"')
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()

        elif 'calc' in query:
            os.startfile("calc.bat")
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()
            #raise Exception("Premature End")
            #sys.exit(0)
            #os.system('cmd /k "explorer.exe shell:appsFolder\Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"')
            
        elif 'rol' in query or 'nel' in query:
            os.system('cmd /k "explorer.exe shell:appsFolder\Microsoft.Windows.ControlPanel"')
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()

        elif 'rome' in query: #check  for one
            os.system('cmd /k "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"')
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()
            
        elif 'ython' in query or 'dle' in query or 'ide' in query and 'video' not in query:
            os.startfile("C:\Program Files (x86)\Python36-32\Lib\idlelib\idle.pyw")
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()
                
        elif 'word' in query or 'world' in query:
            os.system('cmd /k "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe"')
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()

        elif 'ppt' in query or 'power' in query or 'point' in query:
            os.system('cmd /k "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"')
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()

        elif 'flix' in query:
            os.system('cmd /k "explorer.exe shell:appsFolder\4DF9E0F8.Netflix_mcm4njqhnhss8!Netflix.App"')
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()
            
        elif 'run' in query:
            os.system('cmd /k "explorer.exe shell:appsFolder\Microsoft.Windows.Shell.RunDialog"')
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()
            
        elif 'computer' in query or 'pc' in query:
            os.system('cmd /k "explorer.exe shell:appsFolder\Microsoft.Windows.Computer"')
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()
            
        elif 'desktop' in query or 'home' in query:
            os.startfile("C:\\Users\\prakh\\Desktop")
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()
                
        elif 'weather' in query:
            os.system('cmd /k "explorer.exe shell:appsFolder\Microsoft.BingWeather_8wekyb3d8bbwe!App"')
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()

        elif 'shot' in query: #test this fx
            try:
                a = a+1
                name = str(a) + 'shot'
                #os.system('cmd /k "MODE CON COLS=30 LINES=2"')
                
                myScreenshot = pyautogui.screenshot()
                myScreenshot.save(f'{name}.png')
            except:
                a = 0
                name = str(a) + 'shot'
                myScreenshot = pyautogui.screenshot()
                myScreenshot.save(f'{name}.png')

            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()
            

        elif 'pad' in query:
            os.startfile("C:\\Windows\\system32\\Notepad.exe")
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()

        elif 'instagram' in query:
            os.system('cmd /k "explorer.exe shell:appsFolder\Facebook.InstagramBeta_8xx8rvfyw5nnt!Instagram"')
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()
                
        elif 'keyboard' in query:
            os.system('cmd /k ""%windir%\\system32\\osk.exe"" ')
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()
                
        elif 'paint' in query or 'draw' in query:
            os.system('cmd /k ""%windir%\system32\mspaint.exe"" ')
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()

        elif 'gallery' in query:
            os.system('cmd /k "explorer.exe shell:appsFolder\Microsoft.Windows.Photos_8wekyb3d8bbwe!App" ')
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()
                
        elif 'camera' in query:
            os.startfile("D:\\project-final year\\X\\camera.bat")
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()
            #raise SystemExit


        
            

        elif ('pic' in query or 'photo' in query): # prakher will give 
            os.startfile("C:\\Users\\prakh\\source\\repos\\PythonApplication4\\PythonApplication4\\CommandCam.exe")
            time.sleep(3)
            os.system('cmd /k ""C:\\Users\\prakh\\source\\repos\\PythonApplication4\\PythonApplication4\\image.bmp""')
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()

        elif 'list' in query:
            if 'show' in query or 'open' in query:
                f = open("todolist.txt",'r')
                print("The todolist reads as:\n", f.read())
            else:
                f = open("todolist.txt",'a')
                speak("Please tell items")
                print("Tell Items")
                f.write(takeCommand())
                f.close()
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()

        elif 'email' in query and 'check' not in query:  #google ke 2 step verification ko on karke gmail app ke access ke liye ek code milega(use it as passwor d)
            os.startfile("D:\\project-final year\\\X\\emale.bat")
            raise Exception("Premature End")
            sys.exit(0)

        elif 'audio' in query and 'text' in query:#change replace
            os.startfile("C:\\Users\\prakh\\source\\repos\\PythonApplication4\\PythonApplication4\\audio2txt.bat")
            raise Exception("Premature End")
            sys.exit(0)

        elif 'audio' in query and 'book' in query: #text to aduio
            os.startfile("C:\\Users\\prakh\\source\\repos\\PythonApplication4\\PythonApplication4\\AudioBook.bat")
            raise Exception("Premature End")
            sys.exit(0)
            

        elif 'alarm' in query: #alarm replace(inside which time format to be undestood)
            os.startfile("C:\\Users\\prakh\\source\\repos\\PythonApplication4\\PythonApplication4\\alarm.bat")
            raise Exception("Premature End")
            sys.exit(0)
            
                    
        elif 'reminder' in query: #replace
            os.startfile("C:\\Users\\prakh\\source\\repos\\PythonApplication4\\PythonApplication4\\remind.bat")
            
            raise Exception("Premature End")
            sys.exit(0)
            
        elif 'check' in query and 'mail' in query:#replace (wiull wokr  with ids)
            os.startfile("C:\\Users\\prakh\\source\\repos\\PythonApplication4\\PythonApplication4\\auto_mail.bat")
            raise Exception("Premature End")
            sys.exit(0)      
            
        elif 'message' in query or 'sms' in query: #replace (pending) sms ata hai 
            os.startfile("C:\\Users\\prakh\\source\\repos\\PythonApplication4\\PythonApplication4\\message.bat")
            raise Exception("Premature End")
            sys.exit(0)

        elif 'video to audio' or 'video 2 audio':#pending
            os.startfile("C:\\Users\\prakh\\source\\repos\\PythonApplication4\\PythonApplication4\\mp4_2_mp3.bat")
            raise Exception("Premature End")
            sys.exit(0)
            
        else:
            query = query.replace(" ", "+")
            webbrowser.open("google.com/search?q=" + query)
            speak("Anything Else")
            print("Anything Else?")
            choice = takeCommand()
            if 'y' in choice:
                a = wishMe()
                
    mains()












    
             
'''os.startfile("C:\\Users\\prakh\\source\\repos\\PythonApplication4\\PythonApplication4\\CommandCam.exe")
msg = MIMEMultipart()
msg["From"] = 'badshahssic@gmail.com'
msg["To"] = 'prakher.srivastava.psit@gmail.com'
msg["Subject"] = 'INTRUDER DETECTED'
body = datetime.datetime.now()
msg.attach(MIMEText(str(body), "plain"))
filename = "image.bmp"
time.sleep(4.5)
attachment = open("C:\\Users\\prakh\\source\\repos\\PythonApplication4\\PythonApplication4\\image.bmp", "rb")
p = MIMEBase('application','octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p) 
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
msg.attach(p)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
            
server.login('badshahssic@gmail.com', 'aysbqagxhhjgguqu')
text = msg.as_string()



server.sendmail('badshahssic@gmail.com', 'prakher.srivastava.psit@gmail.com', text)
playsound("C:\\Users\\prakh\\Downloads\\deduction.mp3")
server.close()                    
'''
