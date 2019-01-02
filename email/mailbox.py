from message import *
from user import *

class Mailbox():
	"""
	>>> from tests import *
	>>> m1.send()
	>>> print(inbox(u2))
	<BLANKLINE>
	<BLANKLINE>
	1. John Doe <johndoe@mail.com> | test
	<BLANKLINE>
	<BLANKLINE>
	"""
	def __init__(self, user, box_name):
		self.name = box_name
		self.user = user
		self.messages = []

		#self.user.mailboxes += [self]

		self._is_inbox = False
		self._is_sent = False

		if box_name == 'Inbox':
			self._is_inbox = True
		elif box_name == 'Sent':
			self._is_sent = True

	def __repr__(self):
		i = 0
		result = '\n'
		for m in self.messages:
			result += f'\n{i+1}. ' + m.info_line()
			i += 1
		return result + '\n\n'

	def add_to_box(self, email):
		self.messages += [email]

	def num_messages(self):
		return len(self.messages)















if __name__ == '__main__':
	import doctest
	doctest.testmod()