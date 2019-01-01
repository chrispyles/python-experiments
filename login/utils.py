def make_user(last, first, username, password):
	return {
		'last_name': last,
		'first_name': first,
		'username': username,
		'password': password
	}

def get_ln(user):
	return user['last_name']

def get_fn(user):
	return user['first_name']

def get_username(user):
	return user['username']

def get_password(user):
	return user['password']