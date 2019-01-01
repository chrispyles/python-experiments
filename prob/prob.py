from datascience import *

class dist():
	'''Probability distribution object'''
	def __init__(self):
		self.vals = []
		self.probs = []

	def __repr__(self):
		results = '\n'
		results += str(['Value', 'Probability']) + '\n'
		for i,j in zip(self.vals, self.probs):
			results += str([i,j]) + '\n'

		return results

	def values(self, v):
		self.vals = v
		return self

	def probabilities(self, p):
		if sum(p) != 1:
			raise Exception(f'Warning: probabilities sum to {sum(p)}')
		self.probs = p
		return self

	def probability_function(self, f):
		if sum([f(i) for i in self.vals]) != 1:
			raise Exception(f'Warning: probabilities sum to {sum(p)}')
		self.probs = [f(i) for i in self.vals]
		return self

	def ev(self):
		return sum([i*j for i,j in zip(self.vals, self.probs)])

	def ev_squared(self):
		return sum([i**2 * j for i,j in zip(self.vals, self.probs)])

	def sd(self):
		return (self.ev_squared() - self.ev())**0.5














