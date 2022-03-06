import sys

if (len(sys.argv) != 2):
	print('Error')
	sys.exit()
count = sys.argv[1]
i = 0
for line in sys.stdin:
	i += 1
	result = line.replace("\n", "")
	if (i > int(count)):
		break
	if (len(result) != 32):
		continue
	if (result.startswith("00000") and result[5] != '0'):
		print(result)
