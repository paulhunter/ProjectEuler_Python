
import operator
import time

def main():
	t = time.clock()
	count = 0
	f = open('p54data.txt')
	for l in f.readlines():
		h1,h2 = readHands(l)
		if compareHands((determineHand(h1),determineHand(h2))):
			count += 1
	print "Answer: %d" % count
	print "Time Taken: %0.3f seconds" % (time.clock()-t)


def readHands(line):
	cards = line.split(' ')
	hand1 = []
	hand2 = []
	for a in range(0,5):
		hand1.append(card(cards[a]))
	for a in range(5,10):
		hand2.append(card(cards[a]))
	hand1 = sorted(hand1, key=operator.attrgetter('value'))
	hand2 = sorted(hand2, key=operator.attrgetter('value'))
	return (hand1,hand2)

def compareHands(hands):
	x,y = hands
	if x[0] != y[0]:
		return (True if x[0]>y[0] else False)
	else:
		for i in range(1,len(x)):
			if x[i]!=y[i]:
				return (True if x[i]>y[i] else False)


#Returns Tupes that have (score, secondScore, thirdScore, ...)
#Scores:
#  High Card 		(0,highestCard, 0)
#  One Pair 		(1,Pair Value, highest Single)
#  Two Pair 		(2,Pair Value, Second Pair Value, remainder)
#  Three of a Kind 	(3,TripleValue, hRemainder, lRemainder)
#  Straight 		(4,highCard)
#  Flush 			(5,highCard)
#  Full House		(6,tripleValue,pairValue)
#  Four of a Kind 	(7,quadValue,remainder)
#  Straight Flush 	(8,highCard)
#  Royal Flush 		(9)
def determineHand(h):
	#if All the cards are of the same suit
	if sum([(1 if h[i].suit == h[i+1].suit else 0) for i in range(len(h)-1)])==4:
		#if we have a royal flush
		if sum([u.value for u in h]) == 14+13+12+11+10:
			return (9,)
		#if we have a straight flush
		if reduce(operator.mul, [(1 if h[i].value == h[i+1].value - 1 else 0) for i in range(len(h)-1)], 1) == 1:
			return (8,h[4].value)
		return (5,h[4].value,h[3].value,h[2].value,h[1].value,h[0].value)

	else:
		if reduce(operator.mul, [(1 if h[i].value == h[i+1].value - 1 else 0) for i in range(len(h)-1)], 1) == 1:
			return (4,h[4].value)
		#Four of a kind
		if h[1].value == h[2].value == h[3].value == h[4].value:
			return (7,h[4].value,h[0].value)
		if h[0].value == h[1].value == h[2].value == h[3].value:
			return (7,h[0].value,h[4].value)

		#check for three of a kind and subsequently full houses
		if h[0].value == h[1].value == h[2].value:
			if h[3].value == h[4].value:
				return (6,h[0].value,h[3].value)
			else:
				return (3,h[0].value,h[4].value, h[3].value)
		if h[2].value == h[3].value == h[4].value:
			if h[0].value == h[1].value:
				return (6,h[3].value,h[1].value)
			else:
				return (3,h[3].value,h[1].value,h[0].value)
		if h[1].value == h[2].value == h[3].value:
			return (3,h[2].value, h[4].value, h[0].value)

		#Check for two of a kind
		if h[0].value == h[1].value:
			if h[2].value == h[3].value:
				return(2,h[2].value, h[1].value, h[4].value)
			elif h[3].value == h[4].value:
				return(2,h[3].value, h[1].value, h[2].value)
			else:
				return(1,h[1].value,h[4].value,h[3].value,h[2].value)
		if h[1].value == h[2].value:
			if h[3].value == h[4].value:
				return(2,h[3].value, h[1].value, h[0].value)
			else:
				return(1,h[1].value,h[4].value,h[3].value,h[0].value)
		if h[2].value == h[3].value:
			if h[0].value == h[1].value:
				return(2,h[3].value, h[1].value, h[4].value)
			else:
				return(1,h[2].value,h[4].value,h[1].value,h[0].value)
		if h[3].value == h[4].value:
			if h[0].value == h[1].value:
				return(2,h[3].value, h[1].value, h[2].value)
			elif h[1].value == h[2].value:
				return(2,h[3].value, h[1].value, h[0].value)
			else:
				return(1,h[3].value,h[2].value,h[1].value,h[0].value)

		return (0, h[4].value, h[3].value, h[2].value, h[1].value, h[0].value)
		#return highcard

Hands = ['High Card', 'One Pair', 'Two Pair', 'Three of a Kind', 'Straight', 'Flush', 'Full House', 'Four of a Kind', 'Straight Flush', 'Royal Flush']
def printHand(hand):
	result = determineHand(hand)[0]
	return "%s %s %s %s %s (%s)" % (tuple([p.__repr__() for p in hand],) + (Hands[result],))




cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
class card:
	def __init__(self,x):
		self.suit = x[1]
		self.value = int(cards.index(x[0])+2)
	def __repr__(self):
		return "%s%s'" % (cards[self.value-2], self.suit)


if __name__ == '__main__':
	main()


