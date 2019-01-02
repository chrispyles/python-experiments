from user import *

class Message():
	"""
	>>> from tests import *
	>>> print(m1.info_line())
	John Doe <johndoe@mail.com> | test
	"""

	messages = []

	def __init__(self, sender, receiver, subject, content):
		self._sender = sender
		self._receiver = receiver
		self.subject = subject
		self._content = content
		self._read = False

		Message.messages += [self]

		#return self

	def __repr__(self):
		result = f'\n\nFROM: {print(self.sender)}'
		result += f'\nTO: {print(self.receiver)}'
		result += f'\n\n{self.content}'
		return result

	def open(self):
		print(self)
		self._read = True

	def set_unread(self):
		self._read = False

	def info_line(self):
		result = f'{self._sender} | {self.subject}'
		return result

	def send(self):
		self._receiver.receive_email(self)
		self._sender.send_email(self)















if __name__ == '__main__':
	import doctest
	doctest.testmod()