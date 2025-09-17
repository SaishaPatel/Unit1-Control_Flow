# ========================================
# ACCELERATED PYTHON UNIT 2 - LESSON 1
# Conditionals: JavaScript to Python
# ========================================

# ========================================
# SECTION 1: QUICK TRANSLATION CHALLENGE
# ========================================
print("==Grade Classification==")
score = 87
if score >= 90:
    print("A grade!")
elif score >= 80:
    print("B grade!")
else:
    print("Below B")

# ========================================
# SECTION 2: AGE CATEGORY CLASSIFIER
# ========================================
age_input = input("Enter your age:")
if age_input:
    age = int(age_input)
    
    if 12 >= age >= 0:
        print("You are a child")
    elif 19 >= age >= 13:
        print("You are a teenager")
    elif 64 >= age >= 20:
        print("You are an adult")
    elif age >= 65:
        print("You are a senior")
    else:
        print("Please enter a valid age")
else:
    print("Please enter a valid age")

# ========================================
# SECTION 3: STUDENT STATUS CHECKER
# ========================================


# ========================================
# SECTION 4: GRADE VALIDATOR CHALLENGE
# ========================================


# ========================================
# SECTION 5: WEATHER DECISION SYSTEM
# ========================================
