import sys

# Elements of Programming Interviews in Python
#
# Chapter 5: Strings

# warmup
#
# reorder the array's entries so that the even entries appear first
def even_odd_array(arr):
	"""
	arr: List[Int]
	rtype: List[Int]
	"""
	n = len(arr)

	even, odd = 0, n -1

	while even < odd:
		num = arr[even]

		if num % 2 == 1:
			arr[even], arr[odd] = arr[odd], arr[even]
			odd -= 1

		else:
			even += 1

	return arr

# 5.1 The Dutch National Flag Problem
#
# Partition about a selected pivot
def dutch_flag_partition(pivot_ind, arr):
	"""
	pivot_ind: Int
	arr: List[Int]
	rtype: List[Int]
	"""
	n = len(arr)

	piv = arr[pivot_ind]
	less, equal, greater = 0, 0, n

	while equal < greater:
		num = arr[equal]

		if num > piv:
			greater -= 1
			arr[equal], arr[greater] = arr[greater], arr[equal]

		elif num == piv:
			equal += 1

		else: #less than piv
			arr[equal], arr[less] = arr[less], arr[equal]
			equal += 1
			less += 1

	return arr

# 5.2 Increment an Arbitrary-Precision Integer
#
# D + 1, return in array
def plus_one(arr):
	"""
	arr: List[Int]
	rtype: List[Int]
	"""
	n = len(arr)

	arr[-1] += 1
	carryOn = 0

	for i in reversed(range(n)):
		arr[i] += carryOn

		if arr[i] >= 10:
			carryOn = arr[i] / 10
			arr[i] %= 10
		else:
			carryOn = 0

	if carryOn:
		arr = [carryOn] + arr

	return arr

# 5.3 Multiply Two Arbitrary-Precision Integers
#
# Multiply two numbers given in arrays
def multiply(num1, num2):
	"""
	num1: List[Int]
	num2: List[Int]
	rtype: List[Int]
	"""
	n = len(num1)
	m = len(num2)

	isPos = (num1[0] < 0) == (num2[0] < 0)

	num1[0], num2[0] = abs(num1[0]), abs(num2[0])

	res = [0] * (n+m)

	for i in reversed(range(n)):
		for j in reversed(range(m)):
			res[i+j+1] += num1[i] * num2[j]
			res[i+j] += res[i+j+1] / 10
			res[i+j+1] %= 10

	for i in range(len(res)):
		if res[i] == 0:
			res = res[i+1:]
		elif i == len(res) -1:
			res = [0]
		else:
			break

	if not isPos:
		res[0] *= -1

	return res



# 5.4 Advancing Through an Array
#
# Check wether its possible to advance through the array, in which each element 
# represents the step a player can take at the spot
def advance_by_offset(arr):
	"""
	arr: List[Int]
	rtype: List[Int]
	"""

	return [] 

# 5.5 Delete Duplicates From a Sorted Array
#
# Delete duplicates
def delete_duplicates(arr):
	"""
	arr: List[Int]
	rtype: List[Int]
	"""
	n = len(arr)
	write = 1

	for i in range(1, n):
		if arr[i] != arr[write -1]:
			arr[write] = arr[i]
			write += 1

	return arr[:write]

# 5.6 Buy and Sell a Stock Once
#
#
def buy_and_sell_stock_once(arr):
	"""
	arr: List[Int]
	rtype: Int
	"""
	max_profit, smallest = 0, float('inf')

	for num in arr:
		if num < smallest:
			smallest = num
		else:
			max_profit = max(max_profit, num - smallest)

	return max_profit

# 5.9 Enumerate All Primes to N
#
#
def generate_primes(n):
	"""
	n: Int
	rtype: List[Int]
	"""
	if n < 3:
		return [2]

	res = [2]

	def isPrime(num):
		for prime in res:
			if num % prime == 0:
				return False

		return True

	for i in range(3,n):
		if isPrime(i):
			res.append(i)

	return res


def run(num):
	if num == "0":
		arr = [1,2,3,4,5,6,7] 
		expected = [6,2,4,5,3,7,1]

		result = even_odd_array(arr)

		if result == expected:
			return "Warmup correct!"  
		else: 
			return "Warmup incorrect"

	elif num == "1":
		arr = [0,1,2,0,2,1,1]
		pivot1 = 3
		expected1 = [0,0,2,2,1,1,1]

		res1 = dutch_flag_partition(pivot1, arr) == expected1

		pivot2 = 2
		expected2 = [[0,1,0,1,1,2,2], [0,0,1,1,1,2,2]]

		res2 = dutch_flag_partition(pivot2, arr) in expected2


		if res1 and res2:
			return "Question 5.1 correct!"  
		else: 
			return "Question 5.1 incorrect" 

	elif num == "2":
		arr1 = [1,2,9]
		expected1 = [1,3,0]
		res1 = plus_one(arr1) == expected1

		arr2 = [9,9]
		expected2 = [1,0,0]
		res2 = plus_one(arr2) == expected2


		if res1 and res2:
			return "Question 5.2 correct!"  
		else: 
			return "Question 5.2 incorrect" 

	elif num == "3":
		num1 = [1,9,3,7,0,7,7,2,1]
		num2 = [-7,6,1,8,3,8,2,5,7,2,8,7]

		expected1 = [-1,4,7,5,7,3,9,5,2,5,8,9,6,7,6,4,1,2,9,2,7]

		res1 = multiply(num1, num2) == expected1

		num3 = [2,5]
		num4 = [2,5]

		expected2 = [6,2,5]

		res2 = multiply(num3, num4) == expected2

		if res1 and res2:
			return "Question 5.3 correct!"  
		else: 
			return "Question 5.3 incorrect" 

	elif num == "4":
		arr1 = [3,2,0,0,2,0,1]
		expected1 = False
		res1 = advance_by_offset(arr1) == expected1

		arr2 = [3,2,1,0,2,0,1]
		expected2 = True
		res2 = advance_by_offset(arr2) == expected2

		if res1 and res2:
			return "Question 5.4 correct!"  
		else: 
			return "Question 5.4 incorrect" 

	elif num == "5":
		arr = [1,2,2,3,4,4,5,6]
		expected = [1,2,3,4,5,6]

		res = delete_duplicates(arr) == expected

		if res:
			return "Question 5.5 correct!"  
		else: 
			return "Question 5.5 incorrect" 

	elif num == "6":
		arr1 = [5,1,2,3,6,2,12]
		expected1 = 11
		res1 = buy_and_sell_stock_once(arr1) == expected1

		arr2 = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
		expected2 = 30
		res2 = buy_and_sell_stock_once(arr2) == expected2

		if res1 and res2:
			return "Question 5.6 correct!"  
		else: 
			return "Question 5.6 incorrect" 

	elif num == "9":
		expected = [2,3,5,7,11,13,17,19]
		res = generate_primes(20) == expected

		if res:
			return "Question 5.9 correct!"  
		else: 
			return "Question 5.9 incorrect" 


	return "Not a valid question"


print(run(sys.argv[1]))