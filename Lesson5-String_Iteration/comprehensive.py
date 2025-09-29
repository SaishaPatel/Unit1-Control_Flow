# Part 3 - Comprehensive Analysis
password = input("Enter a password: ")

length = len(password)
upper_counter = 0
lower_counter = 0
digit_counter = 0

for char in password:
    if 'A' <= char <= 'Z':
        upper_counter +=1
    elif 'a' <= char <= 'z':
        lower_counter +=1
    elif '0' <= char <= '9':
        digit_counter +=1

print(f"Upper: {upper_counter}")
print(f"Lower: {lower_counter}")
print(f"Digit: {digit_counter}")

if upper_counter > 0 and lower_counter > 0 and digit_counter >0:
    rating = "STRONG"
else:
    rating = "WEAK"

print(f"Password: {password} Strength: {rating}")

# Practice Problem 2
# word = "Pass123"

# length = len(word)
# upper_counter = 0
# lower_counter = 0
# digit_counter = 0

# long_enough = False
# has_upper = False
# has_lower = False
# has_digit = False

# for char in word:
#     if 'A' <= char <= 'Z':
#         upper_counter +=1
#         has_upper = True
#     if 'a' <= char <= 'z':
#         lower_counter +=1
#         has_lower = True
#     if '0' <= char <= '9':
#         digit_counter +=1
#         has_digit = True
    

# if length >= 8:
#     long_enough = True

# if long_enough and has_upper and has_lower and has_digit:
#     strength = "STRONG"
# else:
#     strength = "WEAK"

# print(f"Password: {word} is {strength}")

# Practice Problem 3
# text = "hello"

# repeats = False

# for i in range(len(text) - 2):
#     if text[i] == text[i+1] == text[i+2]:
#         repeats = True

# if repeats == True:
#     print("REPEATS")
# else:
#     print("NO REPEATS")