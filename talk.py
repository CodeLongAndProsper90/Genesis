"""
talk.py
Created on 11/13/19 by CodeLongAndProsper90

Requires:
    data.py: settings
    log.py: log()
    gtts: gTTS
"""
def assistant_speaks(output):
        import threading as Threading
        from data import settings
        from log import log
        from gtts import gTTS
        import os
        toSpeak = gTTS(text = output, lang =settings['voice'], slow = False) 
        # saving the audio file given by google text to speech 
        toSpeak.save('.output.mp3') 
        
        os.system('play -q .output.mp3 &')
        log( 'Genisis: ' + output)
        print("Genisis : ", end = '')
        Type(output)

def speak(text):
    assistant_speaks(text)


def Type(s):
    import sys, time
    s = s + "\n"
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
