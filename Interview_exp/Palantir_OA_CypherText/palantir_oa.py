# Hello World program in Python


def decrypt(char, shift, isReversed=False):
    _range = ord("z") - ord("a") + 1
    base = ord("a")

    value = ord(char) + shift - base
    value %= _range

    if isReversed:
        return chr(ord("z") - value)

    return chr(value + base)


def question1(string, key):
    shift = key
    res = ""

    for char in string:
        if not char.isalpha():
            res += char
        else:
            res += decrypt(char, shift)

        if char.isdigit():
            shift += int(char)

    return res


print question1("he2l9lo wo1rld@", 3)


def question2(string, key):
    shift = key
    res = ""

    stack = []

    for char in string:
        if char.isalpha():
            if stack:
                to_shift = int("".join(stack))
                stack = []
                shift += to_shift

            res += decrypt(char, shift)

        elif char.isdigit() or char == "-":
            stack.append(char)
            res += char

        else:
            res += char

    return res


print question2("he12l9lo wo-1rld", 7)


def question3(string, key):
    shift = key
    res = ""

    stack = []
    isReversed = False

    for char in string:
        if char.isalpha():
            if stack:
                to_shift = int("".join(stack))
                stack = []
                shift += to_shift

            res += decrypt(char, shift, isReversed)

        elif char.isdigit() or char == "-":
            stack.append(char)
            res += char

        elif char == "!":
            isReversed = not isReversed
            res += char

        else:
            res += char

    return res


print question3("he12!l9lo wo!-1rld", 12)


def question4(string, key):
    shift = key
    res = ""

    stack = []
    scope_stack = []
    isReversed = False

    for char in string:
        if char.isalpha():
            if stack:
                to_shift = int("".join(stack))
                stack = []
                shift += to_shift

            res += decrypt(char, shift, isReversed)

        elif char.isdigit() or char == "-":
            stack.append(char)
            res += char

        elif char == "!":
            isReversed = not isReversed
            res += char

        elif char == "(":
            if stack:
                to_shift = int("".join(stack))
                stack = []
                shift += to_shift

            scope_stack.append(shift)
            res += char

        elif char == ")":
            shift = scope_stack.pop()
            res += char

        else:
            res += char

        print char, shift, scope_stack

    return res


print question4("he12(!l(9lo w)o!-1r)ld", 30)
