#IMPORTANT: enable imap from settings in your gmail account

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


# Importing libraries 
import imaplib, email
import tkinter as tk
from tkinter import simpledialog

user = 'prakher.srivastava.psit@gmail.com'
#password = '' TO BE ENTERED


ROOT = tk.Tk()

ROOT.withdraw()

# the input dialog
speak("please enter your email id")
SENDER_INP = simpledialog.askstring(title="Check Mail",
                                  prompt="What's your EmailId?")

speak("please enter your password")
PASSWORD = simpledialog.askstring(title="Check Mail",
                                  prompt="What's your 2 Way Auth Password?")

speak("please enter recipient email id")
RECEIVER_INP = simpledialog.askstring(title="Check Mail",
                                  prompt="Whose Email you want to check?")

print("Fetching...")
speak("fetching last email")

imap_url = 'imap.gmail.com'




# Function to get email content part i.e its body part 
def get_body(msg): 
	if msg.is_multipart(): 
		return get_body(msg.get_payload(0)) 
	else: 
		return msg.get_payload(None, True) 

# Function to search for a key value pair 
def search(key, value, con): 
	result, data = con.search(None, key, '"{}"'.format(value)) 
	return data 

# Function to get the list of emails under this label 
def get_emails(result_bytes): 
	msgs = [] # all the email data are pushed inside an array 
	for num in result_bytes[0].split(): 
		typ, data = con.fetch(num, '(RFC822)') #he Internet RFC 822 specification defines an electronic message format consisting of header fields and an optional message body.
		msgs.append(data) 

	return msgs 

# this is done to make SSL connnection with GMAIL 
con = imaplib.IMAP4_SSL(imap_url) 

# logging the user in 
con.login(SENDER_INP, PASSWORD) 

# calling function to check for email under this label 
con.select('Inbox') 

# fetching emails from user
msgs = get_emails(search('FROM', RECEIVER_INP, con)) 

# Uncomment this to see what actually comes as data 
#print(msgs) 


# Finding the required content from our msgs 
# User can make custom changes in this part to 
# fetch the required content he / she needs 

# printing them by the order they are displayed in your gmail 
for msg in msgs[::-1]: 
	for sent in msg: 
		if type(sent) is tuple: 

			# encoding set as utf-8 
			content = str(sent[1], 'utf-8') 
			data = str(content) 

			# Handling errors related to unicodenecode 
			try: 
				indexstart = data.find("ltr") 
				data2 = data[indexstart + 5: len(data)] 
				indexend = data2.find("</div>") 

				# printtng the required content which we need 
				# to extract from our email i.e our body
				idxstart = data2.find("From") #added to shrink o/p otherwise data was too much
				short = data2[idxstart: indexend] #shrinked but still some non req data
				
				idxstart =short.find('From:')
				idxend = short.find('Message-ID:')
				short2 = short[idxstart: idxend]

				idxstart = short.find('Subject:')
				idxend = short.find("Content-Type:")
				short3 = short2 + short[idxstart: idxend]

				idxstart = short.find('charset="UTF-8"')
				idxend = short.find("Content-Type: text/html;")
				short4 = short3 + short[idxstart+15: idxend-32]

				print(short4)
				#speak(short4)

			except UnicodeEncodeError as e: 
				pass
		break #added to check only last mail coz all mail can be too much and will hang the system
	break #remove this break to have all the messages (not sure all, but yes many and dont know if the break above this one is also stopping some or not
	
print("Anything else?")
speak("Anything else")
choice = takeCommand()
if 'y' in choice:
    os.startfile("C:\\Users\\prakh\\source\\repos\\PythonApplication4\\PythonApplication4\\PythonApplication4.bat")
else:
    pass  
