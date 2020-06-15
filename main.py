from multiplication import multiply
from division import divide
from register import *

a = int(input())
b = int(input())


r_a = store_in_register(a)
r_b = store_in_register(b)


if DEBUG:
	print(r_a,r_b)


binary_product = multiply(r_a, r_b)
binary_quotient, binary_remainder = divide(r_a, r_b)
decimal_product = convert_decimal(binary_product)
decimal_quotient = convert_decimal(binary_quotient)
decimal_remainder = convert_decimal(binary_remainder)


print("decimal product:", decimal_product)
print("decimal_quotient:", decimal_quotient)
print("decimal_remainder:", decimal_remainder)
print("binary_product:", binary_product)
print("binary_quotient", binary_quotient)
print("binary_remainder", binary_remainder)


assert(decimal_product == convert_to_decimal(binary_product))
assert(decimal_quotient == convert_to_decimal(binary_quotient))
assert(decimal_remainder == convert_to_decimal(binary_remainder))