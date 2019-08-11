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
	arr: List[Int]
	rtype: List[Int]
	"""

	return []

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

# 5.5

# 5.6


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

		return "3"

	return "Not a valid question"


print(run(sys.argv[1]))