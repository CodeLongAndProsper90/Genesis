def systemp(command_linux, command_win):
    from sys import platform
    from os import system
    if platform == 'linux':
        system(command_linux)
    elif platform.lower() == 'windows':
        system(command_win)
