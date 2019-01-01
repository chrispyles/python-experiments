from utils import *

class User:
	def __init__(self, ln, fn, un, pw):
		self.last = ln
		self.first = fn
		self.user = un
		self.pw = pw

	def change_pw(self, old_pw, new_pw):
		if old_pw == self.pw:
			self.pw = new_pw

cpyles = make_user('Pyles', 'Chris', 'cpyles', 'rf3r.WLS')
