from message import *
from user import *

class Mailbox():
	"""
	>>> from tests import *
	>>> m1.send()
	>>> print(inbox(u2))
	<BLANKLINE>
	<BLANKLINE>
	John Doe <johndoe@mail.com> | test
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
		result = '\n'
		for m in self.messages:
			result += m.info_line()
		return result + '\n\n'

	def add_to_box(self, email):
		self.messages += [email]















if __name__ == '__main__':
	import doctest
	doctest.testmod()