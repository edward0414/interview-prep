import sys

# quora question link: https://www.quora.com/Computer-science-is-not-teaching-me-programming-it-is-teaching-me-maths-What-can-I-do-to-use-my-coding-knowledge-to-program-apps-etc-Any-suggestions-on-how-to-teach-myself-to-program-Any-useful-websites-videos-etc/answer/Gayle-Laakmann-McDowell

# Question 3


def hello(name):
    print("hello " + name)

# Question 4


def isPrime(num):
    num = int(num)
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

# Question 5


def allPrimes(num):
    num = int(num)
    primes = [2]
    if num < 2:
        return "no valid prime in the range"
    if num < 3:
        return primes

    for i in range(3, num + 1):
        if isPrime(i):
            primes.append(i)

    return primes

# Question 6


def sieveOfEratosthenes(num):
    num = int(num)
    if num < 2:
        return "no valid prime in the range"

    lst = [True] * num  # careful about the indices
    lst[0] = False

    for i in range(2, int(num**0.5) + 1):
        if lst[i-1]:
            temp = i**2
            while temp <= num:
                lst[temp - 1] = False
                temp += i

    result = []
    for i in range(num):
        if lst[i]:
            result.append(i+1)

    return result

# Question 7


def primeFact(num):
    num = int(num)
    if num < 2:
        return "no valid prime fact for this number"

    res = []
    remainder = num

    while not isPrime(remainder):
        for i in range(2, int(remainder**0.5)+1):
            if remainder % i == 0:
                res.append(i)
                remainder /= i
                break

    res.append(remainder)

    return res

# Question 8


class Person:
    lst = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.lst.append((name, age))

    @classmethod
    def sort(cls):

        cls.lst.sort(key=lambda ele: ele[1], reverse=True)
        return cls.lst

    # Question 9
    @classmethod
    def sortByComparator(cls):
        def comparator(ele1, ele2):
            return ele2[1] - ele1[1]

        cls.lst.sort(cmp=comparator)
        return cls.lst


def run(num, args):
    if num == "3":
        return hello(args)
    elif num == "4":
        return isPrime(args)
    elif num == "5":
        return allPrimes(args)
    elif num == "6":
        return sieveOfEratosthenes(args)
    elif num == "7":
        return primeFact(args)
    elif num == "8":
        edward = Person("Edward", 21)
        jocelyn = Person("Jocelyn", 24)
        lan = Person("Lan", 38)
        tower = Person("Tower", 20)
        robbie = Person("Robbie", 23)

        return Person.sort()

    elif num == "9":
        edward = Person("Edward", 21)
        jocelyn = Person("Jocelyn", 24)
        lan = Person("Lan", 38)
        tower = Person("Tower", 20)
        robbie = Person("Robbie", 23)

        return Person.sortByComparator()

    return "Not a valid question"


print(run(sys.argv[1], sys.argv[2]))
