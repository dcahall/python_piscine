import sys

def make_sound(func):
	def wrapper(*argc, **kwargs):
		print('SQUEK')
		res = func(*argc, **kwargs)
		return res
	return wrapper 
		

@make_sound
def add_ingot(purse):
	if purse and purse.get('gold_ingots') < 0:
		print('The wallet cannot contain a negative amount of gold_ingots')
		sys.exit(1)
	if purse.get('gold_ingots') == None:
		purse['gold_ingots'] = 1
	else:
		purse['gold_ingots'] = purse.get('gold_ingots') + 1
	return purse

@make_sound
def get_ingot(purse):
	if purse and purse.get('gold_ingots') < 0:
		print('The wallet cannot contain a negative amount of gold_ingots')
		sys.exit(1)
	if purse.get('gold_ingots') != 0 and purse.get('gold_ingots', 0) != 0:
		purse['gold_ingots'] = purse.get('gold_ingots') - 1
	if purse.get('gold_ingots') == 0:
		purse.pop('gold_ingots')
	return purse


@make_sound
def empty(purse):
	if purse and purse.get('gold_ingots') < 0:
		print('The wallet cannot contain a negative amount of gold_ingots')
		sys.exit(1)
	if purse.get('gold_ingots') != None:
		purse.pop('gold_ingots')
	return purse
