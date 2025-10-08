print("====== User Registration =====\n")

while True:
    username = input("Enter a username: ")
    if len(username) < 3:
        print("Too Short! 3 characters minimum!")
        continue
    if len(username) > 15:
        print("Too Long! Maximum 15 characters!")
        continue
    # Checking for spaces
    has_space = False
    for char in username:
        if char == " ":
            has_space = True
    if has_space:
        print("Username can't have spaces!")
        continue
    # Username validation passed
    print(f"Username '{username}' accepted! \n")
    break

while True:
    password = input("Enter a password: ")
    if len(password) < 8:
        print("Password is too short! 8 characters minimum!")
        continue
    # Check for digits and uppercase letters
    has_digit = False
    has_upper = False
    for char in password:
        if "0" <= char <= "9":
            has_digit = True
        if "A" <= char <= "Z":
            has_upper = True
    if not has_digit:
        print("Password must have a digit!")
        continue
    if not has_upper:
        print("Password must contain an uppercase letter!")
        continue
    # Password validation passed
    print("Password accepted! \n")
    break

while True:
    age = input("Enter your age: ")
    if age.isdigit():
        if int(age) < 13:
            print("Must be 13+ to register!")
            continue
        elif int(age) > 120:
            print("Please enter a valid age!")
            continue
    else:
        print("Please enter a valid number!")
        continue
    # Age validation passed!
    print(f"Age {age} recorded! \n")
    break

while True:
    confirmation = input("To confirm and complete registration, type 'yes' or 'y'. To cancel, type 'no' or 'n': ")
    if confirmation.lower() == "yes" or confirmation.lower() == 'y':
        print("Registration successful!!")
        print(f"Welcome, {username}")
    elif confirmation.lower() == "no" or confirmation.lower() ==  'n':
        print("Registration cancelled.")
    else:
        print("Please enter 'yes' or 'no'")
        continue
    break