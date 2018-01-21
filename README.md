# UndergraduateThesis
Solving the Penney Ante Problem with Conway's Algorithm. Proof using Markov Chains, Martingales, and a Combinatoric Approach

# Conway's Algorithm
Conway invented an algorithm which returns X. The code is
```python
class Conway(object):
	def __init__(self, n):
		"""
		Usage:
		game = Conway(n)
		Conway.n = the length of the sequences
		Conway.combinations = all possible combinations of A
		Conway.expectedValues[A] = the expected waiting time for A
		Conway.probabilities[A][B] = probability of A coming before B
		"""
		self.n = n

		# Generate all possible combinations
		self.combinations = []
		def gen(s):
			if len(s) < n:
				gen(s+'H')
				gen(s+'T')
			elif len(s) == n:
				self.combinations.append(s)
		gen('')

		# generate expected values
		self.expectedValues = {}
		for combination in self.combinations:
			self.expectedValues[combination] = self.calculateExpectedWaitingTime(combination)

		# generate table of probabilities. A dict of dict Dict[A]beats[B]
		self.probabilities = {}
		for A in self.combinations:
			self.probabilities[A] = {}
			for B in self.combinations:
				self.probabilities[A][B] = self.calculateProbability(A, B)


	def conwaysAlgorithm(self, A, B):
		"""
		Conway's Algorithm
		For explanation, see README
		"""
		binaryRepresentation = [0] * len(A)

		for i in range(len(A)):
			n = len(A) 

			if  A[i: n] == B[0: n-i]:
				binaryRepresentation[i] = 1

		decimal = 0

		for i in range(len(binaryRepresentation)):
			index = len(binaryRepresentation) - i - 1
			decimal += binaryRepresentation[index] * 2**i

		return float(decimal)

	def calculateProbability(self, A, B):
		if A == B:
			return None
		else:
			AA = self.conwaysAlgorithm(A, A)
			BB = self.conwaysAlgorithm(B, B) 
			AB = self.conwaysAlgorithm(A, B) 
			BA = self.conwaysAlgorithm(B, A)  

			# This is the odds a will precede B
			odds = (AA - AB) / ((BB - BA))
			return 1.0/(odds + 1.0)

	def calculateExpectedWaitingTime(self, A):
		return 2*self.conwaysAlgorithm(A, A)

	def findAnomolies(self):
		"""
		Returns a list of anomolies
		An anomoly is a list of 2-tuples of sequences such that 
		self.expectedValue(A) < self.expectedValue(A) and
		   probabilities[A][B] < probabilities[B][A]
		See README
		   
		anomoly = [(A,B), (C,D), ... ] 
		"""
		anomolies = []

		for A in self.combinations:
			for B in self.combinations:
				if self.probabilities[A][B] != None and (1.0 - self.probabilities[A][B]) < 0.5:
					pass
					# print 'E({}):{} | E({}):{} | P({}, {}):{}'.format(A, self.expectedValues[A], B, self.expectedValues[B], A, B, self.probabilities[A][B])
					

				if self.probabilities[A][B] == None:
					pass
				# elif (self.expectedValues[A] > self.expectedValues[B]) and self.probabilities[A][B] < 0.5:
				# 	# print "!"
				# 	anomolies.append((A,B))

				elif ((self.expectedValues[A] == self.expectedValues[B])):
					# print "!"
					anomolies.append((A,B))

		return anomolies

	def findCycles(self):
		pass

```

# Abstract  
Imagine a two player game where each player is assigned a sequence, for example THTH and HTHH, and a coin is flipped until either player sees their sequence. The first player to see their sequence appear wins. Given two sequences, which sequence is expected to come first in the sequence of coin flips? What is the probability of a certain player winning? Although these two questions sound similar, the result is that in our example, the expected number of turns for sequence A to appear is 20 and for B it is 18. Meanwhile, the probability of A winning is 9/14 while the probability of B winning is 5/14. Additionally the game has the property that for any sequence A chooses, B can always find a sequence that has a higher probability of winning. These counterintuitive results are the core of the Penney Ante problem, discovered by Walter Penney [3]. My thesis will study this problem through three approaches based in Markov chains, martingales, and a combinatoric approach.

# Poster 
![Saleh's Thesis](http://i.imgur.com/KczPx55.jpg)

# Contact
For any questions comments concerns please contact shindi@haverford.edu
