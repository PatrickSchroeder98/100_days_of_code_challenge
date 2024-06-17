# ########DEBUGGING############


# # Describe Problem
# def my_function():
# 	for i in range(1,20):
# 		if i == 20:
# 			print("You got it!")
# my_function()
# The range function stops at i = 19. Solution: modify to range(1, 21) or i == 19
# depending on what program needs to accomplish.
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it!")


my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])
# Randint can produce 6, which is larger than highest index of list. It also ignores index 0.
from random import randint

dice_imgs = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
# 	print("You are a millenial.")
# elif year > 1994:
# 	print("You are a Gen Z.")
# If a year is equal to 1994, there is no code to execute. Solution: elif statement should have year >= 1994
# or if should have year <= 1994.
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}")
# Solutions: no indentation before print statement, age must be converted to int,
# string inside print must be converted to f-string.
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}")


# # Print is Your Friend
# pages = 0
# words_per_page = 0
# pages = int(input("Number of pages: "))
# words_per_page == int(input("Number of words per page: "))
# total_words = pages * words_per_page
# print(pages)
# print(words_per_page)
# print(total_words)
# Print shows that words_per_page is still equal to 0. Solution: fix the mistake with == in 59 line.
pages = 0
words_per_page = 0
pages = int(input("Number of pages: "))
words_per_page = int(input("Number of words per page: "))
total_words = pages * words_per_page
print(total_words)

# # Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#     b_list.append(new_item)
#     print(b_list)
# Solution b_list.append(new_item) should be indented, so every new_item gets appended on b_list


def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])


# # Debugging Odd or Even
# number = int(input()) # Which number do you want to check?
#
# if number % 2 = 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")
# Solution: mistake in line 98, shoud be ==. Optionally input could ask the question in comment to make the user
# experience better.
number = int(input("Wchich number do you want to check?"))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# # Debugging Leap Year
# Which year do you want to check?
# year = input()
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")
# Solution: convert input to int, optionally message for better user experience.
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")


# # Debugging Fizz Buzz
# target = int(input())
# for number in range(1, target + 1):
#     if number % 3 == 0 or number % 5 == 0:
#         print("FizzBuzz")
#     if number % 3 == 0:
#         print("Fizz")
#     if number % 5 == 0:
#         print("Buzz")
#     else:
#         print([number])
# Solution: first if should use and operator, next ifs should be changed to elifs, print shouldn't print number in list,
# optional message for user experience.
target = int(input("Select the range of FizzBuzz program."))
for number in range(1, target + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
