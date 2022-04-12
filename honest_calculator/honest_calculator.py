message = ["Enter an equation\n",
		"Do you even know what numbers are? Stay focused!",
		"Yes ... an interesting math operation. You've slept through all classes, haven't you?",
		"Yeah... division by zero. Smart move...",
		"Do you want to store the result? (y / n):",
		"Do you want to continue calculations? (y / n):",
		" ... lazy",
		" ... very lazy",
		" ... very, very lazy",
		"You are",
		"Are you sure? It is only one digit! (y / n)",
		"Don't be silly! It's just one number! Add to the memory? (y / n)",
		"Last chance! Do you really want to embarrass yourself? (y / n)"]


def error_handling(msg, memory):
	print(msg)
	string = input(message[0]).split()
	return check_m(string, memory)

def check_digit(string):
	try:
		float(string[0])
		float(string[2])
	except Exception:
		return False
	else:
		return True

def check_sign(sign):
	if sign != '-' and sign != '+' and sign != '*' and sign != '/':
		return False
	elif len(sign) > 1:
		return False	
	return True

def calculate(string):
	try:
		if string[1] == '/':
			res = float(string[0]) / float(string[2])
		elif string[1] == '*':
			res = float(string[0]) * float(string[2])
		elif string[1] == '+':
			res = float(string[0]) + float(string[2])
		elif string[1] == '-':
			res = float(string[0]) - float(string[2])
	except Exception:
		return False
	else:
		return res
		
def check_m(string, memory):
	if string[0] == 'M':
		string[0] = str(memory)
	if string[2] == 'M':
		string[2] = str(memory)
	return string

def ask_store_simply_res(message_index):
	while True:
		answer = input(message[message_index])
		if answer == 'y':
			if message_index < 12:
				message_index += 1
				continue
			break
		if answer == 'n':
			return True


def store_result(res):
	answer = input(message[4])
	if answer == 'y':
		if is_one_digit(res) and ask_store_simply_res(10):
			return False
		return True
	elif answer == 'n':
		return False
	store_result(res)

def continue_calculation():
	answer = input(message[5])
	if answer == 'y':
		return True
	elif answer == 'n':
		return False
	continue_calculation()

def is_one_digit(value):
	if value > -10 and value < 10 and value.is_integer():
		return True
	return False

def check(x, y, oper):
	msg = ""
	if is_one_digit(x) and is_one_digit(y):
		msg = msg + message[6]
	if x == 1 or y == 1 and oper == '*':
		msg = msg + message[7]
	if x == 0 or y == 0 and oper in ('*', '+', '-'):
		msg = msg + message[8]
	if len(msg):
		print(message[9] + msg)

memory = 0
string = input(message[0]).split()
string = check_m(string, memory)
while True:
	if not check_digit(string):
		string = error_handling(message[1], memory)
		continue 
	if not check_sign(string[1]):
		string = error_handling(message[2], memory)
		continue
	check(float(string[0]), float(string[2]), string[1])
	res = calculate(string)
	if type(res) is type(True):
		string = error_handling(message[3], memory)
		continue
	print(res)
	if store_result(res):
		memory = res
	if continue_calculation():
		string = input(message[0]).split()
		string = check_m(string, memory)
		continue
	break
