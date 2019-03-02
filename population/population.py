import pandas as pd
import numpy as np
from individual import *

class Population:
	"""

	>>> p = Population('name', 'age', 'height')
	>>> chris = Individual('Chris', p, {'age' : 20, 'height' : 70})
	>>> p.attributes()
	['age', 'height']
	>>> chris.__repr__()
	'ID: Chris\\n\\tage: 20\\n\\theight: 70'
	>>> p._size
	1
	>>> chris.set_attribute('age', 21)
	age: 20 -> 21
	>>> p.mean('age')
	20.0
    """

	def __init__(self, primary_key, *args):
		self._attributes = []
		self._size = 0
		self._members = []
		for arg in args:
			self._attributes += [arg]

		self._df = pd.DataFrame(columns = self._attributes)

	def add_member(self, member):
		self._members += [member]
		self._size += 1
		self._df = self._df.append(member.attributes(), ignore_index=True)

	def show(self):
		return self._df

	def attributes(self):
		return self._attributes

	def members(self):
		return [member.primary_key for member in self._members]

	def mean(self, attribute):
		return np.mean(self._df[attribute])

	def median(self, attribute):
		return self._df[attribute].quantile()

	def mode(self, attribute):
		return self._df[attribute].mode()

	def remove_member(self):
		print('Which individual would you like to remove?')
		for i in range(len(self._members)):
			print(f'\n{i+1}. {self._members[i].primary_key}')
		to_delete = int(input()) - 1
		del self._members[to_delete]































if __name__ == '__main__':
	import doctest
	doctest.testmod()