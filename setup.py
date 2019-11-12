def setup():
    from git import run_git
    from time import sleep
    from sound import play
    print('Entering setup.')
    run_git('pull origin master')
    print('Welcome to Genesis.')
    print('What is your language?')
