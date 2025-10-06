# Input Validation 1 - Username Validation
while True:
    username = input("Enter a username (3-15 characters): ")
    if len(username) < 3:
        print("Too short! Minimum 3 characters!")
        continue
    if len(username) > 15:
        print("Too long! Max 15 characters!")
        continue
    # Check if username has any space
    has_space = False
    for char in username:
        if char == ' ':
            has_space = True
    if has_space:
        print("No spaces allowed!")
        continue
    # Username validation passed
    print(f"Username '{username}' accepted! \n")
    break