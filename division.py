from register import *


def divide(divident, divisor):
	global REGISTER_LENGTH
	negative_divident = isNegative(divident)
	negative_divisor = isNegative(divisor)

	if(negative_divident):
		divident = twos_complement(divident)
	if(negative_divisor):
		divisor = twos_complement(divisor)

	remainder = divident
	quotient = [0] * REGISTER_LENGTH

	# Multiply divisor by 2^LENGTH
	for i in range(LENGTH + 1):
		shift_left(divisor)


	if DEBUG:
		print("step", 0,"\t\t\t\t", divisor, remainder, quotient)
	# Division
	for i in range(LENGTH + 1):
		shift_right(divisor)
		remainder = subtract(remainder, divisor)
		if isNegative(remainder):
			add(remainder, divisor)
			shift_left(quotient, 0)
		else:
			shift_left(quotient, 1)
		if DEBUG:
			print("step", i,"\t\t\t\t", divisor, remainder, quotient)

	if not negative_divisor and not negative_divident:
		pass
	if not negative_divisor and negative_divident:
		add(quotient, [0] * (REGISTER_LENGTH - 1) + [1])
		quotient = twos_complement(quotient)
		subtract(remainder, divisor)
		remainder = twos_complement(remainder)
	if negative_divisor and not negative_divident:
		add(quotient, [0] * (REGISTER_LENGTH - 1) + [1])
		quotient = twos_complement(quotient)
		subtract(remainder, divisor)
	if negative_divisor and negative_divident:
		subtract(remainder, divisor)

	return quotient, remainder

