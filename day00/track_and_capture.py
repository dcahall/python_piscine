import sys

required_len = 5
required_widht = 3
strings = []

def error_message():
	print('Error')
	sys.exit(1)


def	parse_symbol(i, line, symbol, char_occurance):
	if i == 0:
		if char_occurance != 2 or line[4] != symbol or line[0] != symbol:
			return False
	if i == 1:
		if char_occurance != 4 or line[2] == symbol:
			return False
	if i == 2:
		if char_occurance != 3 or line[3] == symbol or line[1] == symbol:
			return False
	return True


for line in sys.stdin:
	str = line.replace("\n", "")
	if len(str) != required_len:
		error_message()
	strings.append(str)
if len(strings) != required_widht:
	error_message()


symbol = strings[0][0]	
char_occurance = 0
i = 0
for word in strings:
	for char in word:
		if char == symbol:
			char_occurance += 1
	veracity = parse_symbol(i, word, symbol, char_occurance)
	i += 1
	char_occurance = 0
	if veracity == False:
		print('False')
		sys.exit(0)	 
print('True')
