import math
import argparse
import sys

def	new_i(i):
	return (i / (12 * 100))

def	annuity_payment(principal,  i, periods):
	if principal < 0 or i < 0 or periods < 0:
		print("Incorrect parameters")
		quit()
	i = new_i(i)
	fraction = (i * (1 + i)**periods) / ((1 + i)**periods - 1)
	monthly_payment = math.ceil(principal * fraction)
	print(f"Your monthly payment = {monthly_payment}!")
	print(f"Overpayment = {int(monthly_payment * periods - principal)}")

def	annuity_principal(payment,  i, periods):
	if payment < 0 or i < 0 or periods < 0:
		print("Incorrect parameters")
		quit()
	i = new_i(i)
	fraction = (i * (1 + i)**periods) / ((1 + i)**periods - 1)
	principal = int(payment / fraction)
	print(f"Your loan principal = {principal}!")
	print(f"Overpayment = {int(payment * periods) - principal}")

def	annuity_periods(payment, i, principal):
	if payment < 0 or i < 0 or principal < 0:
		print("Incorrect parameters")
		quit()
	i = new_i(i)
	bracket = payment / (payment - i * principal)
	periods = math.ceil(math.log(bracket, 1 + i))
	print_periods(periods)
	print(f"Overpayment = {int(payment * periods - principal)}")

def	print_periods(num_month):
	num_years = num_month // 12
	if num_years == 1:
		print(f"It will take {num_years} year", end='')
	elif num_years > 1:
		print(f"It will take {num_years} years", end='')
	if num_month % 12 == 1:
		print(f" and {num_month % 12} month", end='')
	elif num_month % 12 > 1:
		print(f" and {num_month % 12} month", end='')
	print(" to repay this loan!")

def	annuity_calculation(args):
	if args.interest:
		if args.periods and args.principal:
			annuity_payment(args.principal, args.interest, args.periods)
		elif args.payment and args.periods:
			annuity_principal(args.payment, args.interest, args.periods)
		elif args.payment and args.principal:
			annuity_periods(args.payment, args.interest, args. principal)
		else:
			print("Incorrect parameters")
			quit()
	else:
		print("Incorrect parameters")
		quit()

def	diff_calculation(args):
	if not args.principal or not args.periods or not args.interest:
		print("Incorrect parameters")
		quit()
	month = 1
	total = 0
	for month in range(month, args.periods + 1):
		bracket = args.principal - (args.principal * (month - 1))/args.periods
		i = new_i(args.interest)
		diff_payment = math.ceil(args.principal / args.periods + i * bracket)
		print(f"Month {month}: payment is {diff_payment}")
		total += diff_payment
	print(f"Overpayment = {total - int(args.principal)}")

parser = argparse.ArgumentParser("Enter the values required for the calculation")
parser.add_argument("--type", help="What calculation do you need to perform differentiation or annuity?")
parser.add_argument("--principal", type=float, help="The amount that you want to borrow?")
parser.add_argument("--periods", type=int, help="Number of months required to repay the loan")
parser.add_argument("--interest", type=float, help="Annual percentage")
parser.add_argument("--payment", type=float, help="The amount of the monthly payment.")
args = parser.parse_args()
if args.type == "annuity":
	annuity_calculation(args)
elif args.type == "diff":
	diff_calculation(args)
else:
	print("Incorrect parameters")