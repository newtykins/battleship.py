from modules.utils import cls, BANNER, exitGame, hasPlayed
from modules.singleplayer import startSingleplayer
from modules.leaderboards import viewLeaderboards
import modules.formatting as formatting
import time

def onboarding():
	cls()
	playerName = input(formatting.bold(formatting.green("""
Hello, I'm Battleship.py! What is your name?\n
""")))
	if hasPlayed(playerName):
		greeting = 'Welcome back'
	else:
		greeting = 'It\'s nice to meet you'
	print(formatting.red("""
%s, %s! Enjoy the game! <3
	""") % (greeting, playerName))
	time.sleep(2)
	cls()
	return playerName

def mainMenu(name: str):
	error = False
	print(BANNER)
	print("""
%s, please select an option:

1) Singleplayer
2) Leaderboards
3) Exit
	""" % (name))
	while True:
		try:
			choice = int(input('Your choice: '))
			if choice == 1:
				startSingleplayer(name)
			elif choice == 2:
				viewLeaderboards(name)
			elif choice == 3:
				exitGame(name)
			break
		except ValueError:
			print('Please enter a valid option!')
			error = True
			break
	if error:
		cls()
		mainMenu(name)
		return