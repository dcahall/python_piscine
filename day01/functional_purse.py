import sys

def add_ingot(purse):
	if purse and purse.get('gold_ingots') < 0:
		print('The wallet cannot contain a negative amount of gold_ingots')
		sys.exit(1)
	if purse.get('gold_ingots') == None:
		purse['gold_ingots'] = 1
	else:
		purse['gold_ingots'] = purse.get('gold_ingots') + 1
	return purse


def get_ingot(purse):
	if purse and purse.get('gold_ingots') < 0:
		print('The wallet cannot contain a negative amount of gold_ingots')
		sys.exit(1)
	if purse.get('gold_ingots') != 0 and purse.get('gold_ingots', 0) != 0:
		purse['gold_ingots'] = purse.get('gold_ingots') - 1
	if purse.get('gold_ingots') == 0:
		purse.pop('gold_ingots')
	return purse


def empty(purse):
	if purse and purse.get('gold_ingots') < 0:
		print('The wallet cannot contain a negative amount of gold_ingots')
		sys.exit(1)
	if purse.get('gold_ingots') != None:
		purse.pop('gold_ingots')
	return purse
