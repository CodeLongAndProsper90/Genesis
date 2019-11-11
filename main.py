#importing speech recognition package from google api 
import speech_recognition as sr 
from gtts import gTTS # google text to speech 
import os # to save/open files 
import wolframalpha # to calculate strings into formula 
from selenium import webdriver # to control browser operations 
from playsound import playsound
from data import settings
from time import ctime, time
print(settings)

def log(msg):
    global settings
    if settings['debug'] == True:
        log = open('.genisislog', 'a')
        log.write(str(ctime(time())) + ' : ' + msg + '\n')
        log.close()

def assistant_speaks(output): 
        global settings, log
        print("Genisis : ", output)
        log( 'Genisis: ' + output)
        toSpeak = gTTS(text = output, lang =settings['voice'], slow = False) 
	# saving the audio file given by google text to speech 
        toSpeak.save('.output.mp3') 
	
	# playsound package is used to play the same file.
        #os.system('play -q .output.mp3')



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




def parse_for(start, end, string):
    global log
    log('SYSTEM : parsefor called')
    return string[string.find(start)+len(start):string.rfind(end)]

def process_text(Input): 
    global settings, log
    if 'how are you' in Input:
        log('YOU: Input is how are you')
        speak('I am fine.')
    elif 'clear log' in Input:
        if settings['debug'] ==  True:
            log = open('.genisislog', 'w')
            log.write('         ===LOG CLEARED BY GENISIS ON ' + ctime(time()) + '===           \n')
            log.close()
            speak('I\'ve cleared the log.')
        else:
            speak('I\'m sorry, ' + settings['name'] + ', I can\'t let you do that')
            Input = ''
    if 'edit' or 'open' in Input:
        log('COMMAND: edit')
        if 'edit' in Input:
            start = 'edit'
        elif 'open' in Input:
            start = 'open'
        
        if 'with' or 'in' in Input:
            if 'with' in Input:
                end = 'with'
            elif 'in' in Input:
                end = 'in'
            filename = parse_for(start, end, Input).strip()
            print(filename)
            i = Input.split(' ')
            editor = i[i.index(end)+1]
            print(editor)
            command = editor + ' ' + filename
            print('Command is :' + command) 
            os.system(command)
        else:
            command = settings['editor'] + Input.strip('edit')
            os.system(command)
            log('SYSTEM; Called os.system in edit. Command is: ' + command)
    else:
        assistant_speaks('Sorry, I don\'t know what you\'re talking about.') 

# Driver Code 
if __name__ == "__main__": 
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
            text = 0

