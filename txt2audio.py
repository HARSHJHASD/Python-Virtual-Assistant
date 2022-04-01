# Import the required module for text 
# to speech conversion 
from gtts import gTTS

import tkinter as tk
from tkinter import simpledialog
ROOT = tk.Tk()
ROOT.withdraw()
TEXT = simpledialog.askstring(title="TEXT2AUDIO", prompt="Enter the text")

#import cric
#print(cric.all_match())

# This module is imported so that we can 
# play the converted audio 
import os 

# The text that you want to convert to audio 
mytext = TEXT

# Language in which you want to convert 
language = 'en'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 

# Saving the converted audio in a mp3 file named 
# welcome 
myobj.save("welcome1.mp3") 

# Playing the converted file 
#os.system("mpg321 welcome.mp3") 
