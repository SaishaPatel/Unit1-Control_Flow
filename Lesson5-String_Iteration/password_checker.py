password = input("Enter your password: ")

# Character Counts
length = len(password)
letter_count = 0
digit_count = 0
special_char_count = 0
uppercase_count = 0
lowercase_count = 0

for char in password:
    if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
        letter_count += 1
    if 'A' <= char <= 'Z':
        uppercase_count += 1
    if 'a' <= char <= 'z':
        lowercase_count += 1
    if '0' <= char <= '9':
        digit_count += 1
    if not ('A' <= char <= 'Z' or 'a' <= char <= 'z' or '0' <= char <= '9' or char == ' '):
        special_char_count += 1

# Security Issues
repeated_chars = False
for i in range(length -2):
    if password[i] == password[i+1] == password[i+2]:
       repeated_chars = True
       

sequence = False
for i in range(length -2):
    if ord(password[i+1]) == ord(password[i]) + 1 and ord(password[i+2]) == ord(password[i]) + 2:
        sequence = True
        break

# Final Rating
if length >= 8 and uppercase_count > 0 and lowercase_count > 0 and digit_count > 0 and special_char_count > 0 and repeated_chars == False and sequence == False:
    rating = "STRONG"
elif length >= 8 and uppercase_count > 0 and lowercase_count > 0 and digit_count > 0 and special_char_count > 0 and (repeated_chars == True or sequence == True):
    rating = "MEDIUM"
else:
    rating = "WEAK"

# Analysis
print("PASSWORD ANALYSIS:")
print("==================")
print(f"Password: '{password}'")

print("CHARACTER COUNTS:")
print(f"Length: {length} characters")
print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase letters: {lowercase_count}")
print(f"Digits: {digit_count}")
print(f"Special Characters: {special_char_count}")

print("REQUIREMENTS CHECK:")
if length >= 8:
        print("✓ Length (8+ characters): PASSED")
else:
    print("x Length (8+ characters): FAILED")
if uppercase_count > 0:
        print("✓ Uppercase letters: PASSED")
else:
    print("x Uppercase letters: FAILED")
if lowercase_count > 0:
        print("✓ Lowercase letters: PASSED")
else:
    print("x Lowercase letters: FAILED")
if digit_count > 0:
        print("✓ Digits: PASSED")
else:
    print("x Digits: FAILED")
if special_char_count > 0:
        print("✓ Special characters: PASSED")
else:
    print("x Special characters: FAILED")

print("SECURITY ISSUES:") 
if repeated_chars == True: 
    print("x Repeated characters! (3+)")
else:
    print("✓ No repeated characters (3+)")

if sequence == True:
    print(f"⚠ Contains sequence '{password[i:i+3]}'")
else:
    print("✓ No sequence")

print(f"FINAL RATING: {rating} ")
if rating == "STRONG":
    print("- ALl requirements met")
if rating == "MEDIUM" and sequence == True:
    print("- All requirements met but has a simple sequence")
if rating == "MEDIUM" and repeated_chars == True:
    print("- All requirements met but has repeated characters")
if rating == "WEAK":
    print("- Requirements not met")