import sys

if (len(sys.argv) != 2):
	print('Error')
	sys.exit()

list = sys.argv[1].split(' ')
for word in list:
	print(word[0], end = '')
