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

# 6.1 String to Integer/ Integer to String
#
# Write an interconvertor


def int_to_string(integer):
    """
    integer: int
    rtype: string
    """
    return ""


def string_to_int(string):
    """
    string: string
    rtype: integer
    """
    return 0

# 6.2 Base Conversion
#
#


def convert_base(string, b1, b2):
    """
    string: string
    b1: int
    b2: b2
    rtype: string
    """
    return ""

# 6.3 Alphabet Encoding
#
# "A" = 1, "D" = 4, "AA" = 27, "ZZ" = 702


def alphabet_encoding(string):
    """
    string: str
    rtype: int
    """
    return 0


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

    return "Not a valid question"


print(run(sys.argv[1]))
