from message import *
from mailbox import *

def inbox(user):
	for box in user.mailboxes:
		if box._is_inbox:
			return box

def sent(user):
	for box in user.mailboxes:
		if box._is_sent:
			return box

class User():
	"""
	>>> from tests import *
	>>> print(u1)
	John Doe <johndoe@mail.com>
	>>> u1.create_mailbox('test box')
	>>> print(u1.mailboxes[2].name)
	test box
	"""
	def __init__(self, name, platform, username, password):
		self.name = name
		self.platform = platform
		self.username = username
		self.password = password
		self.mailboxes = [Mailbox(self, 'Inbox'), Mailbox(self, 'Sent')]
		self._inbox = inbox(self)
		self._sent = sent(self)

	def __repr__(self):
		return f'{self.name} <{self.username}@{self.platform}>'

	def receive_email(self, email):
		self._inbox.add_to_box(email)

	def send_email(self, email):
		self._sent.add_to_box(email)

	def create_mailbox(self, box_name):
		self.mailboxes += [Mailbox(self, box_name)]

	#def move_to_box(self, origin, destination, email):




















if __name__ == '__main__':
	import doctest
	doctest.testmod()