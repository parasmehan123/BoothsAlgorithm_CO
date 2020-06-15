DEBUG = False

LENGTH = 16
REGISTER_LENGTH = 2 * LENGTH
#todo
def add(r1, r2):
	global DEBUG
	global LENGTH
	global REGISTER_LENGTH

	if DEBUG:
		print("add", "\t\t\t\t", r1, r2)

	carry = 0
	for i in range(REGISTER_LENGTH - 1, -1, -1):
		val = int(r1[i] ^ r2[i] ^ carry)
		carry = int((r1[i] and r2[i]) or (r1[i] and carry) or (r2[i] and carry))
		r1[i] = val
	return r1

def subtract(r1, r2):
	global DEBUG
	global LENGTH
	global REGISTER_LENGTH

	if DEBUG:
		print("subtract", "\t\t\t\t",r1, r2)

	temp = twos_complement(r2)
	add(r1, temp)
	return r1

def twos_complement(r):
	global DEBUG
	global LENGTH
	global REGISTER_LENGTH

	if DEBUG:
		print("twos_complement", "\t\t\t\t", r)
	temp = [0] * REGISTER_LENGTH
	for i in range(REGISTER_LENGTH):
		temp[i] = int(not r[i])
	add(temp, [0] * (REGISTER_LENGTH - 1) + [1])
	return temp

def shift_left(r, bit = 0):
	global DEBUG
	global LENGTH
	global REGISTER_LENGTH

	if DEBUG:
		print("shift_left", "\t\t\t\t", r)

	for i in range(REGISTER_LENGTH - 1):
		r[i] = r[i + 1]
	r[-1] = bit

def shift_right(r, bit = 0):
	global DEBUG
	global LENGTH
	global REGISTER_LENGTH

	if DEBUG:
		print("shift_right", "\t\t\t\t", r)

	for i in range(REGISTER_LENGTH - 1, -1, -1):
		r[i] = r[i - 1]
	r[0] = bit

def isNegative(r):
	global DEBUG
	global LENGTH
	global REGISTER_LENGTH

	return r[0] == 1

def store_in_register(x):
	global DEBUG
	global LENGTH
	global REGISTER_LENGTH

	r = [0] * REGISTER_LENGTH
	if x < 0:
		x *= -1
		for i in range(REGISTER_LENGTH - 1, -1, -1):
			r[REGISTER_LENGTH - i - 1] = x // (2**i)
			x = x % (2**i)
		r = twos_complement(r)
	else:
		for i in range(REGISTER_LENGTH - 1, -1, -1):
			r[REGISTER_LENGTH - i - 1] = x // (2**i)
			x = x % (2**i)		
	return r

def arithemetic_shift_right(A, Q, Q0):
	global DEBUG
	global LENGTH
	global REGISTER_LENGTH

	Q0 = Q[-1]

	for i in range(REGISTER_LENGTH-1,0,-1):
		Q[i] = Q[i-1]

	Q[0] = A[-1]

	for i in range(REGISTER_LENGTH-1,0,-1):
		A[i] = A[i-1]

	return Q0

def convert_decimal(R):
	global DEBUG
	global REGISTER_LENGTH

	flag = 1
	if isNegative(R):
		R = twos_complement(R)[:]
		flag = -1

	ans = 0
	for i in range(REGISTER_LENGTH):
		ans += R[i] * (2 ** (REGISTER_LENGTH - i - 1))

	return ans * flag

