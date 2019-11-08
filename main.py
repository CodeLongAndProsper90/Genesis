#importing speech recognition package from google api 
import speech_recognition as sr 
from gtts import gTTS # google text to speech 
import os # to save/open files 
import wolframalpha # to calculate strings into formula 
from selenium import webdriver # to control browser operations 

num = 1
def assistant_speaks(output): 
	global num 

	# num to rename every audio file 
	# with different name to remove ambiguity 
	num += 1
	print("Genisis : ", output)

	toSpeak = gTTS(text = output, lang ='en', slow = False) 
	# saving the audio file given by google text to speech 
	toSpeak.save('.output.mp3') 
	
	# playsound package is used to play the same file. 
	os.system('mpg321 -q .output.mp3')



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
        return audio

def process_text(Input): 
	 try: 
		 if 'search' in Input or 'play' in Input: 
			 # a basic web crawler using selenium 
			 search_web(Input) 
			 return
		 
		 elif "who are you" in Input or "define yourself" in Input: 
			 speak = '''Hello, I am Genisis'''		 
		 elif "who made you" in Input or "created you" in Input: 
			 speak = "I have been created by Code Long And Prosper 90"
			 assistant_speaks(speak) 
			 return
		 
		 elif "geeksforgeeks" in Input:# just 
			 speak = """Geeks for Geeks is the Best Online Coding Platform for learning."""
			 assistant_speaks(speak) 
			 return
			 
		 elif "calculate" in Input.lower(): 
		 
			 # write your wolframalpha app_id here 
			 app_id = "WOLFRAMALPHA_APP_ID" 
			 client = wolframalpha.Client(app_id) 
			 
			 indx = Input.lower().split().index('calculate') 
			 query = Input.split()[indx + 1:] 
			 res = client.query(' '.join(query)) 
			 answer = next(res.results).text 
			 assistant_speaks("The answer is " + answer) 
			 return
		 
		 elif 'open' in Input: 
		 
			 # another function to open 
			 # different application availaible 
			 open_application(Input.lower()) 
			 return
		 
		 else: 
			 
			 assistant_speaks("I can search the web for you, Do you want to continue?") 
			 ans = get_audio() 
			 if 'yes' in str(ans) or 'yeah' in str(ans): 
			    search_web(Input) 
			 else: 
			    return
	 except : 
		 
		 assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?") 
		 ans = get_audio() 
		 if 'yes' in str(ans) or 'yeah' in str(ans): 
		    search_web(Input) 

# Driver Code 
if __name__ == "__main__": 
	assistant_speaks("What's your name, Human?") 
	name ='Human'
	name = get_audio() 
	assistant_speaks("Hello, " + name + '.') 
	
	while(1): 

		assistant_speaks("What can i do for you?") 
		text = get_audio().lower() 

		if text == 0: 
			continue

		if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text): 
			assistant_speaks("Ok bye, "+ name+'.') 
			break

		# calling process text to process the query 
		process_text(text) 

