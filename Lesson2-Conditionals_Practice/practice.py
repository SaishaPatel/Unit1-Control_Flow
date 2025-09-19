age = int(input("Enter your age: "))
rating = input("Enter a movie rating (G/PG/PG-13/R)")

print(f"Age: {age}, Rating: {rating}")

if age:
    if rating == "G":
        print("APPROVED: Anyone can watch!")
    elif rating == "PG":
        if age >= 6:
            print("APPROVED!")
        else:
            print("NOT RECCOMENDED FOR YOUR AGE")
    elif rating == "PG-13":
        if age >= 13:
            print("APPROVED!")
        else:
            print("NOT RECCOMENDED FOR YOU AGE!")
    elif rating == "R":
        if age >= 17:
            print("APPROVED!")
        else:
            print("DENIED! Must be 17+ to wach R-rated")
        
else:
    print("ERROR! Enter your age")