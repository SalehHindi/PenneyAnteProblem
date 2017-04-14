# Calculate correlation AB

import pdb

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

game = Conway(3)
prob = game.probabilities
e = game.expectedValues
anom = game.findAnomolies()

for i in anom:
	pass
	# print i

pdb.set_trace()


for q in range(3, 5, 1):
	game = Conway(q)
	anom = game.findAnomolies()
	e = game.expectedValues
	prob = game.probabilities

	maxPair = None
	for ann in anom:
		A = ann[0]
		B = ann[1]
		# print prob[A][B]

		if maxPair == None:
			maxPair = (A,B)
		elif prob[A][B] > prob[maxPair[0]][maxPair[1]]:
			maxPair = (A,B)

	print 'q={} | E={} | #p_{}={} | pair = ({}, {})'.format(q, e[maxPair[0]], maxPair[0], prob[maxPair[0]][maxPair[1]], maxPair[0], maxPair[1])



# Should take an n and give you a list of all the different waiting times and a table of all Pa Pb combinations
