# Utility functions, including predefined objects for doctests

from message import *
from user import *
from mailbox import *

u1 = User('John Doe', 'mail.com', 'johndoe', 'test')
u2 = User('Jane Doe', 'mail.com', 'janedoe', 'test')

m1 = Message(u1, u2, 'test', 'test email')