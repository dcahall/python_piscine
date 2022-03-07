import sys
from functional_purse import add_ingot, get_ingot, empty

def split_booty(*wallets):

	all_ingots = 0
	first_purse = {}
	second_purse = {}
	third_purse = {}
	for purse in wallets:
		if purse.get('gold_ingots') == None:
			continue
		all_ingots += purse.get('gold_ingots')
		empty(purse)
	if all_ingots >= 3:
		for i in range(0, int(all_ingots/ 3)):
			first_purse = add_ingot(first_purse)
			second_purse = add_ingot(second_purse)
			third_purse = add_ingot(third_purse)
	if all_ingots % 3 != 0:
		first_purse = add_ingot(first_purse)
		if all_ingots % 3 == 2:
			second_purse = add_ingot(second_purse)
	return first_purse, second_purse, third_purse
