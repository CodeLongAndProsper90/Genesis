"""
Main.py
Created by CodeLongAndProsper90 on 11/11/19

Requires:
    speechrecognition
    gtts
    sox
    git
    setup.py
    git.py
    .generc

Main.py is the startup script for Genesis

"""
#importing speech recognition package from google api 
import speech_recognition as sr 
from gtts import gTTS # google text to speech 
import os # to save/open files 
from data import settings
from setup import setup
from time import ctime, time # to get the time
from git import run_git # to update 
import commands # to run commands
from log import *
from talk import *


        # playsound package is used to play the same file.
def get_audio(): 
        """
	rObject = sr.Recognizer() 
	audio = '' 

	with sr.Microphone() as source: 
		print("Speak...") 
		
		# recording the audio using speech recognition 
		audio = rObject.listen(source, phrase_time_limit = 5) 
	print("Stop.") # limit 5 secs 

	try: 

		text = rObject.recognize_google(audio, language ='en-US') 
		print("You : ", text) 
		return text 

	except: 

		assistant_speaks("Could not understand your audio, PLease try again !") 
		return 0
        """
        audio = input('YOU: ')
        log('You: ' + audio)
        return audio



def raw_log(text):
    log = open('.genisislog', 'a')
    log.write(text)
    log.close()






def process_text(Input): 
    global settings, log
    if 'how are you' in Input:
        log('COMMAND : HOW ARE YOU')
        speak('I am fine. You?')
        Input = ''
    elif 'clear log' in Input:
        log("COMMAND : CLEAR LOG")
        commmands.clear_log(settings)
        Input = ''
    elif 'update' in Input:
        commands.update()
        Input = ''
    elif 'search' or 'google' in Input:
        commands.google(Input)
        Input = ''
    elif ' push install' in  Input:
        log('SUDO UPDATE')
        commands.update_install()
        Input = ''
    elif 'edit' or 'open' in Input:
        log("COMMAND : EDIT")
        commands.edit(Input,settings)
        Input = ''
    else:
       speak('Sorry, I don\'t know what you\'re talking about.')
    Input = ''
# Driver Code 
if __name__ == "__main__": 
    try:
        raw_log('           ===START SESSION===         \n')
        speak("Hello, " + settings['name'] + ', how may I help?')
        while(1): 

                text = get_audio().lower() 

                if text == 0: 
                        continue

                if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text): 
                        assistant_speaks("Bye, "+ settings['name']+'.') 
                        raw_log('           ===END SESSION===           \n\n')
                        break

                # calling process text to process the query 
                process_text(text) 
                text = ''
    except KeyboardInterrupt or EOFError: 
        assistant_speaks("Bye, "+ settings['name']+'.') 
        raw_log('           ===END SESSION===           \n\n')


