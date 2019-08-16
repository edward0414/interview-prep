import sys

# Elements of Programming Interviews in Python
#
# Chapter 6: Strings

# warmup
#
# check if palindromic
def is_palindromic(string):
	"""
	string: string
	rtype: bool
	"""
	n = len(string)
	L, R = 0, n-1

	while L < R:
		if string[L] != string[R]:
			return False

		L += 1
		R -= 1

	return True

# 6.1
#


# 6.2 
#


# 6.3
#



# 6.4
#


# 6.5 
#


# 6.6 
#


# 6.9 
#



def run(num):
	if num == "0":
		string = "abcba"
		expected = True

		result = is_palindromic(string)

		if result == expected:
			return "Warmup correct!"  
		else: 
			return "Warmup incorrect"

	elif num == "1":
		return "1"

	elif num == "2":
		return "2"

	elif num == "3":
		return "3"

	elif num == "4":
		return "4" 

	elif num == "5":
		return "5"

	elif num == "6":
		return "6"

	elif num == "9":
		return "9"


	return "Not a valid question"


print(run(sys.argv[1]))