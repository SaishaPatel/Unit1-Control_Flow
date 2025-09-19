age = int(input("Enter your age: "))
rating = input("Enter a movie rating (G/PG/PG-13/R): ")

print(f"Age: {age}, Rating: {rating}")

if age:
    if rating == "G":
        print("APPROVED: You can watch this movie!")
    elif rating == "PG":
        if age >= 6:
            print("APPROVED: You can watch this movie!")
        else:
            print("WARNING: NOT RECCOMENDED FOR YOUR AGE")
    elif rating == "PG-13":
        if age >= 13:
            print("APPROVED: You can watch this movie!")
        else:
            print("WARNING: Not reccomended for your age")
    elif rating == "R":
        if age >= 17:
            print("APPROVED: You can watch this movie!")
        else:
            print("DENIED: Must be 17+ to watch R-rated movies")
else:
    print("ERROR: Please enter your age")