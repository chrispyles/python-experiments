accepted_users = ['cpyles', 'sqadeer', 'chanks']
accepted_passwords = ['rf3r.WLS', '1234', '1234']

from tkinter import *

import time

def login_window():
	window = Tk()

	l1 = Label(window, text="Username:")
	l2 = Label(window, text="Password:")

	t1 = Entry(window, textvariable=StringVar())
	t2 = Entry(window, show='*', textvariable=StringVar())

	def log_in(un, pw):
		for i in accepted_users:
			if i == un:
				if pw == accepted_passwords[accepted_users.index(un)]:
					return True
				else:
					return False
			else:
				return False

	def valid():
		u = t1.get()
		p = t2.get()
		if log_in(u, p):
			print('Access Granted')
			l3 = Label(window, text="Access Granted: %s" %(u))
		else:
			print('Access Denied')
			l3 = Label(window, text="Access Denied: %s" %(u))
		l3.pack()
		start_time = time.time()
		current_time = time.time()
		while current_time <= start_time + 20:
			current_time = time.time()
		l3.pack_forget()
		

	b1 = Button(window, text="Log In", command=valid)

	l1.pack()
	t1.pack()
	l2.pack()
	t2.pack()
	b1.pack()

	window.mainloop()



























