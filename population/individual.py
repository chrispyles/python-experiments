import pandas as pd
import numpy as np
from population import *

class Individual:
	"""

	"""
	def __init__(self, primary_key, pop, attributes):
		self._pop = pop
		self.primary_key = primary_key
		assert type(attributes) == dict, 'attributes arg must be a dictionary'
		for key in attributes.keys():
			assert key in self._pop.attributes(), f'{key} is not in self._pop.attributes()'

		self._attributes = attributes

		for key in self._pop._attributes:
			if key not in self._attributes.keys():
				self._attributes[key] = None

		self._pop.add_member(self)

	def __repr__(self):
		result = f"ID: {self.primary_key}"
		for key in self._pop.attributes():
			result += f"\n\t{key}: {self.attributes()[key]}"
		return result


	def attributes(self):
		# returns attribrutes
		return self._attributes

	def set_attribute(self, attribute, value):
		assert attribute in self._attributes.keys(), f'{key} is not in self.attributes()'
		assert type(value) == type(self._attributes[attribute]), f'{value} is not of same type as {attribute}'
		old_val = self._attributes[attribute]
		self._attributes[attribute] = value

		print(f'{attribute}: {old_val} -> {value}')































if __name__ == '__main__':
	import doctest
	doctest.testmod()