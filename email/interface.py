from user import *
from message import *
from mailbox import *
from statements import *

print('\n\nEnter username:')
username = input()
print('\n\nEnter password:')
password = input()

for user in User.users:
	if username == user.username:
		if password == user.password:
			print(user.inbox())