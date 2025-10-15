# 1
n = 5
safe = 0
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("X", end=" ")
        else:
            print("0", end=" ")
            safe += 1
    print()
print(f"Safe: {safe} ")