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
def Type(s):
    import sys, time
    s = s + "\n"
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

def assistant_speaks(output):
        import threading as Threading
        global settings, log
        def output():
            log( 'Genisis: ' + output)
            print("Genisis : ", end = '')
            Type(output)
        def play():
            toSpeak = gTTS(text = output, lang =settings['voice'], slow = False) 
            # saving the audio file given by google text to speech 
            toSpeak.save('.output.mp3') 
            
            # playsound package is used to play the same file.
            os.system('play -q .output.mp3')
        t1 = Threading.Thread(target=output)
        t2 = Threading.Thread(target=play)
        t1.start()
        log('THREADING: Starting output')
        t2.start()
        log('THREADING: Starting play')
        t1.join()
        t2.join()
        log('THREADING: Threads are done')
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


def speak(text):
    assistant_speaks(text)

def raw_log(text):
    log = open('.genisislog', 'a')
    log.write(text)
    log.close()

def printd(text):
	global settings
	if settings['debug'] == True:
		print(text)
	log(text)





def process_text(Input): 
    global settings, log
    if 'how are you' in Input:
        speak('I am fine. You?')
        Input = ''
    elif 'clear log' in Input:
        commmands.clear_log(settings)
        Input = ''
    elif 'edit' or 'open' in Input:
        commands.edit(Input,settings)
        Input = ''
    elif 'update' in Input:
        commands.update(settings)
        Input = ''
    elif 'search' or 'google' in Input:
        commands.google(Input)
        Input = ''
    elif 'update install' == Input:
        log('SUDO UPDATE')
        commands.update_install(settings)
    else:
        assistant_speaks('Sorry, I don\'t know what you\'re talking about.') 
    Input = ''
# Driver Code 
if __name__ == "__main__": 
    try:
        raw_log('           ===START SESSION===         \n')
        assistant_speaks("Hello, " + settings['name'] + ', how may I help?') 
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


