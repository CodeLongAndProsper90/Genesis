"""
git.py
Created 11/11/19 by CodeLongAndProsper90
Modifed 11/11/19

Requires:
    Linux/Bash
    Git
    os.system

Git.py is a wrapper to run git commands without any output.
"""



from os import system
def run_git(command):
    system('git ' + command)
