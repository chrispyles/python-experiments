from user import *
from message import *
from mailbox import *

User('Chris Pyles', 'mail.com', 'cpyles', 'Pa$$word')
Message(User.users[0], User.users[0], 'test', 'test')
Message.messages[0].send()