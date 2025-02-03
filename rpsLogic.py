import random

class rpsObject:
	def __init__(self):
		self.value = None
		self.weakness = None
		self.name = None

class rock(rpsObject):
	def __init__(self):
		self.value = 'r'
		self.weakness = 'p'
		self.name = 'Rock'

class paper(rpsObject):
	def __init__(self):
		self.value = 'p'
		self.weakness = 's'
		self.name = 'Paper'

class scissors(rpsObject):
	def __init__(self):
		self.value = 's'
		self.weakness = 'r'
		self.name = 'Scissors'

def rpsMake(choice):
	if choice == 'r':
		return rock()
	elif choice == 'p':
		return paper()
	elif choice == 's':
		return scissors()
	else:
		return None

def randomChoice():
	choices = ['r', 'p', 's']
	return rpsMake(random.choice(choices))

def testWin(computer, player):
	if computer.weakness == player.value:
		return 1
	elif computer.value == player.weakness:
		return 2
	else:
		return 0
