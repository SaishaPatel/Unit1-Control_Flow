# Syntax:
'''
initialize variable
while condition (test variable):
    code block
    increment/decrement
'''

# num = 5
# while num > 0:
#     print(num)
#     num -= 1
# print("Blastoff!")

num = 1
total = 0
# while num <= 10:
#     total += num # total = total + num
#     num += 1
# print(f"Sum of numbers 1-10: {total}")

while num <= 10:
    total += num
    if num < 10:
        print(num, end="+")
    else:
        print(num, end="=")
    num += 1
print(total)
print()

# Sum of digits
# Take a user input as int, and sum the digits of it
number = input("Enter a number: ") #1234
sum = 0
# for char in number:
#     print(f"{char} {type(char)}")
#     sum += int(char)
# print(f"Total: {sum}")

i=0
while i<len(number):
    sum += int(number[i])
    i += 1
print(f"Total: {sum}")