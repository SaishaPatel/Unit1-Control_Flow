# The Continue Statment
'''
**continue** = Skip to the next iteration

**Difference form break:**
- **break** -> Exit the loop completely
- **continue** -> Skip current iteration, keep looping
'''

# Example skip 3
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count) #1245