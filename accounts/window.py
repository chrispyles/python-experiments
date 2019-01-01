from accounts import *
from tkinter import *

w = Tk()

acct = 0

def get_account():
	global acct
	acct = int(_acct.get())
	proceed_from_acct()

l_acct = Label(w, text='Please enter account number.')
_acct = Entry(w, textvariable=StringVar())
b_acct = Button(w, text='Next', command=get_account)

txn_type = StringVar()

def reopen():
	_acct.delete(0, END)

	l_txn.pack_forget()
	_txn_type.pack_forget()
	b_txn.pack_forget()

	if txn_type == 'Deposit':
		ld.pack_forget()
		ed.pack_forget()
		bd.pack_forget()

	elif txn_type == 'Withdraw':
		lw.pack_forget()
		ew.pack_forget()
		bw.pack_forget()

	elif txn_type == 'Transfer':
		lt1.pack_forget()
		et1.pack_forget()
		lt2.pack_forget()
		et2.pack_forget()
		bt.pack_forget()

	close.pack_forget()

def proceed_dep():
	amt = int(ed.get())
	accounts[acct].deposit(amt)

	global close
	close = Button(w, text='Close', command=reopen)
	close.pack()

def proceed_wit():
	amt = int(ew.get())
	accounts[acct].withdraw(amt)

	close = Button(w, text='Close', command=reopen)
	close.pack()

def proceed_tra():
	rec = int(et1.get())
	amt = int(et2.get())
	accounts[acct].transfer(rec, amt)

	close = Button(w, text='Close', command=reopen)
	close.pack()

def proceed_from_txn():
	global txn_type
	txn_type = txn_type.get()

	if txn_type == 'Deposit':
		global ld, ed, bd
		ld = Label(w, text='Deposit amount:')
		ed = Entry(w, textvariable=StringVar())
		bd = Button(w, text='Proceed', command=proceed_dep)

		ld.pack()
		ed.pack()
		bd.pack()

	elif txn_type == 'Withdraw':
		global lw, ew, bw
		lw = Label(w, text='Withdrawl amount:')
		ew = Entry(w, textvariable=StringVar())
		bw = Button(w, text='Proceed', command=proceed_wit)

		lw.pack()
		ew.pack()
		bw.pack()

	elif txn_type == 'Transfer':
		global lt1, et1, lt2, et2, bt
		lt1 = Label(w, text='Receive account number:')
		et1 = Entry(w, textvariable=StringVar())
		lt2 = Label(w, text='Withdrawl amount:')
		et2 = Entry(w, textvariable=StringVar())
		bt = Button(w, text='Proceed', command=proceed_tra)

		lt1.pack()
		et1.pack()
		lt2.pack()
		et2.pack()
		bt.pack()

def proceed_from_acct():
	global _txn_type
	global txn_type
	global l_txn
	global b_txn

	l_txn = Label(w, text='Please select transaction type.')
	_txn_type = OptionMenu(w, txn_type, 'Deposit', 'Withdraw', 'Transfer')
	b_txn = Button(w, text='Next', command=proceed_from_txn)

	l_txn.pack()
	_txn_type.pack()
	b_txn.pack()

l_acct.pack()
_acct.pack()
b_acct.pack()

w.mainloop()