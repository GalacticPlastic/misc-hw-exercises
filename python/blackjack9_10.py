# Mary Mederos
# 11/28/2019
# Homework Assignment 9 and 10
# This program allows a user to play a simplified game of blackjack against a computer.

# Import random library:
import random

class Card(object):
	# A card object with a suit and rank.
	RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
	SUITS = ("Spades", "Diamonds", "Hearts", "Clubs")
	def __init__(self, rank, suit):
		# Creates a card with the given rank and suit.
		self.rank = rank
		self.suit = suit

	def __str__(self) :
		# Returns the string representation of a card.
		if self.rank == 1:
			rank = "Ace"
		elif self.rank == 11:
			rank = "Jack"
		elif self.rank == 12:
			rank = "Queen"
		elif self.rank == 13:
			rank = "King"
		else:
			rank = self.rank
		return str(rank) + " of " + self.suit

class Deck(object):
	# A deck containing 52 cards.
	def __init__(self):
		# Creates a full deck of cards.
		self.cards = []
		for suit in Card.SUITS:
			for rank in Card.RANKS:
				c = Card(rank, suit)
				self.cards.append(c)

	def shuffle(self):
		# Shuffles the cards.
		random.shuffle(self.cards)

	def deal(self):
		# Removes and returns the top card or none if the deck is empty.
		if len(self) == 0:
			return None
		else:
			return self.cards.pop(0)

	def __len__(self):
		# Returns the number of cards left in the deck.
		return len(self.cards)

class Player(object):
	# This class represents a player in a blackjack game.
	def __init__(self, cards):
		self.cards = cards

	def __str__(self):
		# Returns string rep of cards and points.
		result = ", ".join(map(str, self.cards))
		result += "\n " + str(self.getPoints()) + " points\n"
		return result

	def hit(self, card):
		self.cards.append(card)

	def getPoints(self):
		# Returns the number of points in the hand.
		count = 0
		for card in self.cards:
			if card.rank > 9:
				count += 10
			elif card.rank == 1:
				count += 11
			else:
				count += card.rank

		# Deduct 10 if Ace is available and needed as 1.
		for card in self.cards:
			if count <= 21:
				break
			elif card.rank == 1:
				count -= 10
		return count

	def hasBlackjack(self):
		# Dealt 21 or not.
		return len(self.cards) == 2 and self.getPoints() == 21

class Dealer(Player):
	# Like a Player, but with some restrictions.
	def __init__(self, cards):
		# Initial state: show one card only.
		Player.__init__(self, cards)
		self.showOneCard = True

	def __str__(self) :
		# Return just one card if not hit yet.
		if self.showOneCard:
			return str(self.cards[0])
		else:
			return Player.__str__(self)

	def hit(self, deck):
		# Add cards while points < 17, then allow all to be shown.
		self.showOneCard = False
		while self.getPoints() < 17:
			self.cards.append(deck.deal())

class Blackjack(object):
	def __init__(self):
		self.deck = Deck()
		self.deck.shuffle()

		# Pass the player and the dealer two cards each
		self.player = Player([self.deck.deal(),
													self.deck.deal()])
		self.dealer = Dealer([self.deck.deal(),
													self.deck.deal()])

	def play(self):
		print("The Dealer drew:\n", self.dealer)
		print("\nThe Player drew:\n", self.player)
	
		# Player hits until user says NO
		while True:
			choice = input("Do you want a hit?\n(Enter [Y]/[y] for yes.): ")
			if choice in ("Y", "y"):
				self.player.hit(self.deck.deal())
				points = self.player.getPoints()
				print("You drew:\n", self.player)
				if points > 21:
					print("Your new total of", playerPoints, "is more than 21. You bust.")
					print("DEALER WINS!")
					break
				elif points == 21:
					print("BLACKJACK!")
			else:
				# Dealer's turn to hit
				self.dealer.hit(self.deck)
				print("\nThe Dealer drew:\n", self.dealer)
				dealerPoints = self.dealer.getPoints()
				playerPoints = self.player.getPoints()

				# Determine the outcome
				if dealerPoints > 21:
					print("Dealer busts and YOU WIN!")
					break
				elif dealerPoints > playerPoints:
					print("The Dealer's total of", dealerPoints, "is greater than or equal to your total of", playerPoints, ".")
					print("DEALER WINS!")
					break
				elif dealerPoints < playerPoints and  \
					playerPoints <= 21:
					print("YOU WIN!")
					break
				elif dealerPoints == playerPoints:
					if self. player.hasBlackjack() and \
						not self.dealer.hasBlackjack():
							print("YOU WIN!")
							break
					elif not self.player.hasBlackjack() and \
						self.dealer.hasBlackjack():
						print("DEALER WINS!")
						break
					else:
						print("There is a tie.")
						break

			playerPoints = self.player.getPoints()
			if playerPoints > 21:
				print("Your new total of", playerPoints, "is more than 21. You bust.")
				print("DEALER WINS!")
				break
			else:
				# Dealer's turn to hit
				self.dealer.hit(self.deck)
				print("The Dealer drew:\n", self.dealer)
				dealerPoints = self.dealer.getPoints()

				# Determine the outcome
				if dealerPoints > 21:
					print("Dealer busts and YOU WIN!")
					break
				elif dealerPoints > playerPoints:
					print("The Dealer's total of", dealerPoints, "is greater than or equal to your total of", playerPoints, ".")
					print("DEALER WINS!")
					break
				elif dealerPoints < playerPoints and  \
					playerPoints <= 21:
					print("YOU WIN!")
					break
				elif dealerPoints == playerPoints:
					if self. player.hasBlackjack() and \
						not self.dealer.hasBlackjack():
							print("YOU WIN!")
							break
					elif not self.player.hasBlackjack() and \
						self.dealer.hasBlackjack():
						print("DEALER WINS!")
						break
					else:
						print("There is a tie.")
						break

# Invoke gampeplay.
game = Blackjack()
while True:
	play_again = input("\nDo you want to play a hand of blackjack?\n(Enter [Y]/[y] for yes.): ")
	if play_again in ("Y", "y"):
		game.play()
	else:
		break

# Prompt user to exit program.
input('Press Any Key to Quit')