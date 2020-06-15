from register import *


def multiply(a, b):

	accumulator = [0] * REGISTER_LENGTH
	Q0 = 0
	A = [0] * REGISTER_LENGTH
	N = REGISTER_LENGTH
	M = None
	Q = None

	M = a[:]
	Q = b[:]

	# print(M,Q," hsdfhjsadfbb")

	while True :

		if Q[-1]^Q0 == 1: 
			if Q0 == 0: 
				# print(A,M)
				A = subtract(A,M)[:]

			else:
				A = add(A,M)[:]
			
		Q0 = arithemetic_shift_right(A,Q,Q0)
		N = N - 1
		if N == 0:
			if DEBUG:
				print(Q)
			return Q