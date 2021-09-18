import os

BANNER = """
  ____          _    _    _             _      _                        
 |  _ \        | |  | |  | |           | |    (_)                       
 | |_) |  __ _ | |_ | |_ | |  ___  ___ | |__   _  _ __     _ __   _   _ 
 |  _ <  / _` || __|| __|| | / _ \/ __|| '_ \ | || '_ \   | '_ \ | | | |
 | |_) || (_| || |_ | |_ | ||  __/\__ \| | | || || |_) |_ | |_) || |_| |
 |____/  \__,_| \__| \__||_| \___||___/|_| |_||_|| .__/(_)| .__/  \__, |
                                                 | |      | |      __/ |
                                                 |_|      |_|     |___/ 
"""

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def exitGame(name):
	cls()
	print('See you next time, %s (:' % (name))
	exit()

currentDir = os.path.dirname(os.path.realpath(__file__))