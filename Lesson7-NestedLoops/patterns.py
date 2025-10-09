# Pyramid Pattern

# STEP BY STEP GUIDE
# Row 0: 4 spaces, 1 star
# Row 1: 3 spaces, 3 stars
# Row 2: 2 spaces, 5 stars
# Row 3: 1 space, 7 stars
# Row 4: 0 spaces, 9 stars

rows = 5
for i in range(1, rows+1):
    for j in range (4, -1):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    print()
