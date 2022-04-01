import pyttsx3
import speech_recognition as sr 
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import os
from playsound import playsound
from tkinter.filedialog import askopenfilename

import tkinter as tk
from tkinter import simpledialog
ROOT = tk.Tk()
ROOT.withdraw()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

SENDER_INP = simpledialog.askstring(title="SEND E-Mail", prompt="Enter Sender's E-mail Id")
PASSWORD = simpledialog.askstring(title="SEND E-Mail", prompt="Enter Password")
#siyrzlytsrryzxhk 
RECEIVER_INP = simpledialog.askstring(title="SEND E-Mail", prompt="Enter Recipient's E-mail Id")

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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(SENDER_INP, PASSWORD)
    server.sendmail(SENDER_INP, to, content)
    server.close()

def sendAttachmentEmail(to, subject, content ):
    msg = MIMEMultipart()
    msg["From"] = SENDER_INP
    msg["To"] = RECEIVER_INP
    msg["Subject"] = subject
    msg.attach(MIMEText(content, "plain"))
    speak("Please select the file")
    filename = askopenfilename()
    attachment = open(filename, "rb")
    print("File Attached")
    p = MIMEBase('application','octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    msg.attach(p)
    content = msg.as_string()
    return content         

try:
    c = 0
    #speak("Please tell recipient email id")
    #to = takeCommand()
    #to = to.replace(" ","")
    print("Please tell the subject")
    speak("please tell the subject")
    subject = takeCommand()
    print("What should I say?")
    speak("What should I say?")
    content = takeCommand()
    print("Sir, is there any attachment?")
    speak("Sir, is there any attachment?")
    attach = takeCommand()
    if 'y' in attach:
        content = sendAttachmentEmail(RECEIVER_INP, subject, content  )
    print("Sir, do you want to schedule it for later?")
    speak("Sir, do you want to schedule it for later?")    
    schedule = takeCommand()
    if 'y' in schedule:
        print("Please tell the time")
        speak("Please tell the time")
        stime = takeCommand()
        a = stime
        if len(stime) == 3:
            stime = '0' + a[0] + ":" + a[1] + a[2]
        else:
            stime = a[0] + a[1] + ":" + a[2] + a[3]
        print("Email to: ", RECEIVER_INP, " has been scheduled for: ", stime)
        print("Anything else")
        speak("Anything else")
        choice = takeCommand()
        if 'y' in choice:
            os.startfile("C:\\Users\\prakh\\source\\repos\\PythonApplication4\\PythonApplication4\\PythonApplication4.bat")
        else:
            pass
        #os.startfile("C:\\Users\\prakh\\source\\repos\\PythonApplication4\\PythonApplication4\\PythonApplication4.bat")    
            
        while(True):    
            if datetime.datetime.now().strftime("%H:%M") == stime:
                sendEmail(RECEIVER_INP, content)
                playsound("C:\\Users\\prakh\\Downloads\\deduction.mp3")
                print("Email has been sent!")
                speak("Email has been sent!")
                
                c = 1
                break
                       
    if c == 0:
        sendEmail(RECEIVER_INP, content)
        playsound("C:\\Users\\prakh\\Downloads\\deduction.mp3")
        print("Email has been sent!")
        speak("Email has been sent!")
        print("Anything else")
        speak("Anything else")
        choice = takeCommand()
        if 'y' in choice:
            os.startfile("C:\\Users\\prakh\\source\\repos\\PythonApplication4\\PythonApplication4\\PythonApplication4.bat")
        else:
            pass
except Exception as e:
    print(e)
    print("Sorry Sir, I am not able to send this email")
    speak("Sorry Sir, I am not able to send this email")    
    os.startfile("C:\\Users\\prakh\\source\\repos\\PythonApplication4\\PythonApplication4\\PythonApplication4.bat")


