from message import *
from mailbox import *

class User():
	"""
	>>> from tests import *
	>>> print(User.users[0].name)
	John Doe
	>>> print(u1)
	John Doe <johndoe@mail.com>
	>>> u1.create_mailbox('test box')
	>>> print(u1.mailboxes[2].name)
	test box
	>>> m1.send()
	>>> u2.check_mail()
	<BLANKLINE>
	<BLANKLINE>
	1. John Doe <johndoe@mail.com> | test
	<BLANKLINE>
	<BLANKLINE>
	"""
	users = []

	def __init__(self, name, platform, username, password):
		self.name = name
		self.platform = platform
		self.username = username
		self.password = password
		self.mailboxes = [Mailbox(self, 'Inbox'), Mailbox(self, 'Sent')]

		User.users += [self]
		#self._inbox = inbox(self)
		#self._sent = sent(self)

	def __repr__(self):
		return f'{self.name} <{self.username}@{self.platform}>'

	def inbox(self):
		for box in self.mailboxes:
			if box._is_inbox:
				return box

	def sent(self):
		for box in self.mailboxes:
			if box._is_sent:
				return box

	def receive_email(self, email):
		self.inbox().add_to_box(email)

	def send_email(self, email):
		self.sent().add_to_box(email)

	def create_mailbox(self, box_name):
		self.mailboxes += [Mailbox(self, box_name)]

	def check_mail(self):
		print(self.inbox())

	#def move_to_box(self, origin, destination, email):




















if __name__ == '__main__':
	import doctest
	doctest.testmod()