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
	n = len(arr)

	less, equal, greater = 0, 0, n-1

# 5.2

# 5.3

# 5.4

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
		expected1 = [0,0,1,2,2,1,1]

		res1 = dutch_flag_partition(pivot1, arr) == expected1

		pivot2 = 2
		expected2 = [[0,1,0,1,1,2,2], [0,0,1,1,1,2,2]]

		res2 = dutch_flag_partition(pivot2, arr) in expected2


		if res1 and res2:
			return "Question 5.1 correct!"  
		else: 
			return "Question 5.1 incorrect" 

	return "Not a valid question"


print(run(sys.argv[1]))