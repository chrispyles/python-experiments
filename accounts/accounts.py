f = __file__

accounts = {}

def show_balances():
	print('\n\n')
	for key in accounts:
		if type(accounts[key].balance) in [int, float]:
			#print(str(accounts[key].acct_id) + ' - ' + accounts[key].name + ': $' + str(accounts[key].balance))
			print(f'{accounts[key].acct_id} - {accounts[key].name}: ${accounts[key].balance}')
		else:
			#print(str(accounts[key].acct_id) + ' - ' + accounts[key].name + ': [' + str(accounts[key].balance) + ']')
			print(f'{accounts[key].acct_id} - {accounts[key].name}: [{accounts[key].balance}]')
	print('\n\n')

class Account:
	balance = 0

	def __init__(self, name, acct_id, duplicate=False):
		global accounts

		if acct_id in accounts:
			raise Exception('Account ID is duplicate')
		elif acct_id < 10000:
			raise Exception('Account ID is too short')

		self.name = name
		self.acct_id = acct_id
		self.txn_history = [['txn_num', 'type', 'amount', 'ending balance'], 'OPEN']
		accounts[acct_id] = self

		# write new account into file
		if not duplicate:
			global f
			var = '_' +  str(self.acct_id)
			file = open(f, 'a')
			file.write('\n' + var + f" = Account('{(self.name)}', {self.acct_id}, duplicate=True)")

	def deposit(self, amount, duplicate=False):
		if 'CLOSED' in self.txn_history:
			print('\n\nError: account is closed\n\n')
			return None

		self.balance += amount
		self.txn_history += [[len(self.txn_history)-1, 'deposit', amount, self.balance]]

		# edit balance in file
		if not duplicate:
			global f
			var = '_' +  str(self.acct_id)
			file = open(f, 'a')
			file.write('\n' + var + f".deposit({amount}, duplicate=True)")

			print('\n\nDeposit complete\nBalance: $' + str(self.balance) + '\n\n')

	def direct_deposit(self, amount, duplicate=False):
		if 'CLOSED' in self.txn_history:
			print('\n\nError: account is closed\n\n')
			return None

		self.balance += amount
		self.txn_history += [[len(self.txn_history)-1, 'direct deposit', amount, self.balance]]

		# edit balance in file
		if not duplicate:
			global f
			var = '_' +  str(self.acct_id)
			file = open(f, 'a')
			file.write('\n' + var + f".direct_deposit({amount}, duplicate=True)")

			print('\n\nDirect deposit complete\nBalance: $' + str(self.balance) + '\n\n')

	def withdraw(self, amount, duplicate=False):
		if 'CLOSED' in self.txn_history:
			print('\n\nError: account is closed\n\n')
			return None

		elif amount > self.balance:
			if not duplicate:
				print('\n\nInsufficient funds\nBalance: $' + str(self.balance) + '\n\n')
		else:
			self.balance -= amount
			self.txn_history += [[len(self.txn_history)-1, 'withdrawl', amount, self.balance]]
			if not duplicate:
				print('\n\nWithdrawl complete\nBalance: $' + str(self.balance) + '\n\n')

		# edit balance in file
		if not duplicate:
			global f
			var = '_' +  str(self.acct_id)
			file = open(f, 'a')
			file.write('\n' + var + f".withdraw({amount}, duplicate=True)")

	def transfer(self, receiver_id, amount, duplicate=False):
		receiver = accounts[receiver_id]
		if 'CLOSED' in self.txn_history:
			print('\n\nError: source account is closed\n\n')
			return None

		elif 'CLOSED' in receiver.txn_history:
			print('\n\nError: receiver account is closed\n\n')
			return None

		elif amount > self.balance:
			print('\n\nInsufficient funds\nBalance: $' + str(self.balance) + '\n\n')
		else:
			self.balance -= amount
			receiver.balance += amount
			self.txn_history += [[len(self.txn_history)-1, 'transfer - out', amount, self.balance]]
			receiver.txn_history += [[len(receiver.txn_history)-1, 'transfer - in', amount, receiver.balance]]

			# edit balance in file
			if not duplicate:
				global f
				var = '_' +  str(self.acct_id)
				file = open(f, 'a')
				file.write('\n' + var + f".transfer({receiver_id}, {amount}, duplicate=True)")

				print(f'\n\nTRANSFER EXECUTED\nSender: {self.name} \nReceiver: {receiver.name} \nAmount: ${amount}\n\n')

	def close(self, duplicate=False):
		if 'CLOSED' in self.txn_history:
			print('\n\nError: account is already closed\n\n')
			return None

		self.balance = 'CLOSED'
		self.txn_history += ['CLOSED']

		if not duplicate:
			global f
			var = '_' +  str(self.acct_id)
			file = open(f, 'a')
			file.write('\n' + var + f".close(duplicate=True)")

			print(f'\n\nACCOUNT CLOSED\n\n')

	def reopen(self, duplicate=False):
		self.txn_history.remove('CLOSED')
		self.balance = 0

		if not duplicate:
			global f
			var = '_' +  str(self.acct_id)
			file = open(f, 'a')
			file.write('\n' + var + f".reopen(duplicate=True)")

			print(f'\n\nACCOUNT REOPENED\n\n')

	def transactions(self):
		print('\n\n')
		for item in self.txn_history:
			print(item)

		print('\n\n')


def print_all_transactions():
	for key in accounts:
		print(accounts[key].name)
		print(accounts[key].transactions())


_10001 = Account('Pyles, Christopher Andrew', 10001, duplicate=True)
_10002 = Account('Cafferty, Raymond James', 10002, duplicate=True)
_10003 = Account('Jameson, Katherine Lee', 10003, duplicate=True)
_10001.deposit(100, duplicate=True)
_10001.transfer(10003, 10, duplicate=True)
_10001.transfer(10003, 10, duplicate=True)
_10001.transfer(10002, 20, duplicate=True)
_10001.transfer(10002, 10, duplicate=True)
_10001.deposit(100, duplicate=True)
_10001.deposit(10, duplicate=True)
_10001.deposit(10, duplicate=True)
_10001.withdraw(10, duplicate=True)
_10002.withdraw(10, duplicate=True)
_10004 = Account('Oliveri, Jonah, Michael', 10004, duplicate=True)
_10004.deposit(1000, duplicate=True)
_10002.direct_deposit(1000, duplicate=True)
_10005 = Account('Seward, Anna Leanne', 10005, duplicate=True)
_10005.deposit(100, duplicate=True)
_10005.close(duplicate=True)
_10006 = Account('Lewicki, Sarah Jean', 10006, duplicate=True)
_10006.deposit(500, duplicate=True)
_10005.reopen(duplicate=True)
_10001.deposit(10, duplicate=True)
_10002.withdraw(100, duplicate=True)
_10001.deposit(10, duplicate=True)
_10001.deposit(10, duplicate=True)
_10001.deposit(100, duplicate=True)
_10001.deposit(100, duplicate=True)
_10001.deposit(100, duplicate=True)
_10001.deposit(100, duplicate=True)
_10001.deposit(100, duplicate=True)
_10001.withdraw(100, duplicate=True)
_10001.deposit(100, duplicate=True)
_10001.deposit(100, duplicate=True)
_10001.deposit(100, duplicate=True)
_10001.deposit(100, duplicate=True)
_10001.deposit(100, duplicate=True)
_10007 = Account('Hart, Chelsea Esme', 10007, duplicate=True)
_10007.close(duplicate=True)
_10007.reopen(duplicate=True)
_10007.deposit(100, duplicate=True)