"""
Commands.py
By CodeLongAndProsper90
Created 11/11/19

Commands.py is a wrapper for the commands used in genesis
It contains no exctable code

Requires:
    os
    log.py: log
    talk.py: speak
"""
import os
from log import log


def parse_for(start, end,s):
    return s[s.find(start)+len(start):s.rfind(end)]

def update():
        from git import run_git
        speak('Starting upgrade')
        run_git('pull origin master')
        speak('Finshed!')
def edit(Input, settings):
        
        if 'edit' in Input:
            start = 'edit'
        elif 'open' in Input:
            start = 'open'

        if ' with ' or ' in ' not in Input:
            command = settings['editor'] + Input.strip('edit')
            #os.system(command)
            command = ''
            log('SYSTEM; Called os.system in edit. Command is: ' + command)
        
        if ' with '  in Input:
            filename = parse_for(start, 'with', Input).strip()
            print(filename)
            i = Input.split(' ')
            editor = i[i.index('with')+1]
            print(editor)
            command = editor + ' ' + filename
            print('Command is :' + command) 
            os.system(command)
            command  = '' 
        
        if ' in '  in Input:
            filename = parse_for(start, 'in', Input).strip()
            print(filename)
            i = Input.split(' ')
            editor = i[i.index('in')+1]
            print(editor)
            command = editor + ' ' + filename
            print('Command is :' + command) 
            os.system(command)
            command = ''

def clear_log(settings):

        if settings['debug'] ==  True:
            log = open('.genisislog', 'w')
            log.write('         ===LOG CLEARED BY GENISIS ON ' + ctime(time()) + '===           \n')
            log.close()
            speak('I\'ve cleared the log.')
        else:
            speak('I\'m sorry, ' + settings['name'] + ', I can\'t let you do that')
def remove_first(Input, ss):
    return Input.replace(ss, '', 1)
def google(Input):
    global settings
    Input = remove_first(Input, 'google')
    Input = remove_first(Input, 'search')
    os.system(settings['browser'] + 'https://google.com/search?q=' + Input)
def update_install(settings):
   from OS import systemp
   from log import printd
   from talk import speak
   systemp('sudo cp -r `pwd`/* /usr/genesis', 'echo')
   print('Updated.')
   speak('Sorry, ' + settings['name'] + ' I can\'t let you do that')

