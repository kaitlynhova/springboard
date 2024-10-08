# import math # used for math functions

# ************
# FIRST PROGRAM
# ************
# student_count = 1000
# rating = 4.99
# is_published = False
# course_name = "Python Programming"

# ************
# SETTING MULTIPLE VARIABLES
# ************
# x, y = 1, 2
# x = y = 1

# ************
# SETTING TYPE
# ************
# STUDENT_COUNT = 1001
# # STUDENT_COUNT: int

# FLOAT = 4.99
# # FLOATSSS: float
# print(type(STUDENT_COUNT))


# AGE: int = 20
# AGE = "Python"
# print(AGE)

# ************
# IMMUTABLE TYPES
# ************
# x: int = 1
# print(id(x))


# ************
# MUTABLE TYPES
# ************
# x: list[int] = [1, 2, 3]
# print(id(x))

# x.append(4)

# print(id(x))

# ************
# STRING SNIPPING
# ************
# COURSE = "Python Programming"
# print(len(COURSE))
# print(COURSE[0])
# print(COURSE[-1])
# print(COURSE[0:3])
# print(COURSE[:3])
# print(COURSE[:])

# ************
# ESCAPE SEQUENCES
# ************
# \"
# \'
# \\
# \n
# message = "Python \"Programming"

# ************
# STRING CONCATENATION
# ************
# FIRST = "first"
# LAST = "last"
# FULL = FIRST + " " + LAST
# FANCY_STRING = f"{FIRST} {LAST}"
# print(FANCY_STRING)

# ************
# STRING FORMATTING
# ************
# COURSE = "  Python Programming"
# print(COURSE.upper())
# print(COURSE.lower())
# print(COURSE.title())
# print(COURSE.strip())
# print(COURSE.lstrip())
# print(COURSE.rstrip())
# print(COURSE.find("Pro"))
# print(COURSE.replace("P", "-"))
# print("Pro" in COURSE)
# print("Pro" not in COURSE)

# ************
# NUMBERS TO BINARY AND HEX
# ************
# x = 10
# x = 0b10    # binary
# print(x)
# print(bin(x))


# x = 0x12c    # hex
# print(x)
# print(hex(x))

# ************
# IMAGINARY NUMBERS
# ************
# # a + bi
# y = 1 + 2j   # j = imaginary number
# print(y)

# ************
# NUMBER DIVISION
# ************
# x = 10 / 3
# y = 10 // 3  # integer division
# z = 10 ** 3  # exponent

# x = x + 1
# x += 1

# print(x, y)


# ************
# MATH OPERATIONS (import math)
# ************
# PI = 3.14
# print(round(PI))
# print(abs(-PI))
# print(math.floor(PI))
# search for python 3 built in functions to learn more

# ***************
# PRINTING TYPES
# ***************

# X = input("x: ")  # run in terminal not apprunner
# print(int(X))
# print(float(X))
# print(bool(X))

# ************
# FALSY VALUES / TRUTHY VALUES
# ************
# Falsy values --> 0, "", None, [], False
# Truthy values --> everything else


# ************
# BASIC FUNCTIONS
# ************
# AGE = 22
# if AGE >= 18:
#     print("Adult")
#     pass #if you dont want to do anything
# elif AGE >= 13:
#     print("Teenager")
# else:
#     print("Child")


# NAME = " "
# if not NAME.strip():
#     print("Name is empty")


AGE = 22

# if AGE >= 18 and AGE < 65:
#     MESSAGE = "Eligible"

# print(MESSAGE)


# MESSAGE = "Eligible" if AGE >= 18 else "Not Eligible"

# print(MESSAGE)


# ***************
# BASIC FOR LOOPS
# ***************
# for x in "Python":
#     print(x)


# for x in ['a', 'b', 'c']:
#     print(x)

# for x in range(5):
#     print(x)


# NAMES = ["John", "Mary"]

# for name in NAMES:
#     if name.startswith("X"):
#         print("Found")
#         break
# else:
#     print("Not Found")

# *****************
# BASIC WHILE LOOPS
# *****************
# GUESS = 0
# ANSWER = 5

# while GUESS != ANSWER:
#     GUESS = int(input("Guess: "))   # input always returns a string
# print("You Win!")


# ***************
# BASIC FUNCTIONS
# ***************
# def increment(number, by):
#     return (number, number + by)


# print(increment(2, 3))


# def multiply(*list):
#     TOTAL = 1
#     for number in list:
#         TOTAL *= number
#     return TOTAL


# print(multiply(2, 3, 4, 5))


# def save_user(**user):
#     print(user["id"])


# save_user(id=1, name="John", age=22)

# message = "a"


# def greet():
#     global message # big no no in programming
#     message = "b"


# greet()
# print(message)


# ***************
# DEBUGGING EXERCISE
# ***************

# def multiply(*numbers):
#     TOTAL = 1
#     for number in numbers:
#         TOTAL *= number
#     return TOTAL


# print("Start")
# print(multiply(1, 2, 3))
# print("End")


# *****************
# FIZZBUZZ EXERCISE
# *****************

# input divisible by 3 = Fizz
# input divisible by 5 = Buzz
# input divisible by 3 and 5 = FizzBuzz
# input not divisible by 3 or 5 = input

# def fizz_buzz(input):
#     fizz = "Fizz" if input % 3 == 0 else ""
#     buzz = "Buzz" if input % 5 == 0 else ""

#     if fizz or buzz:
#         return f"{fizz}{buzz}"
#     else:
#         return input


# print(fizz_buzz(15))
