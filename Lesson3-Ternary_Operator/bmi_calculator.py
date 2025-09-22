height = float(input("Enter your height (inches): "))
weight = float(input("Enter your weight (lbs): "))
bmi = round(float((weight/height**2) * 703), 1)

if not height or not weight:
    print("Please enter both a height and weight value")

if height <= 0 or weight <= 0:
    print("Please enter a positive height and weight value")

category = ("Underweight" if bmi < 18.5 else
            "Normal" if 18.5 <= bmi < 25 else
            "Overweight" if 25 <= bmi < 30 else
            "Obese"
            )

reccomendation = "Maintain weight" if category == "Normal" else "Gain weight" if category == "Underweight" else "Lose weight"
health_risk = "Low" if category == "Normal" else "High" if category == "Obese" else "Moderate"

print("=== BMI CALCULATOR ===")

print(f"Height in inches: {height}")
print(f"Weight in pounds: {weight}")

print("========================")
print("BMI HEALTH REPORT")
print("========================")

print(f"Height: {height} inches ")
print(f"Weight: {weight} lbs")
print(f"BMI: {bmi}")
print(f"Category: {category}")
print(f"Recommendation: {reccomendation}")
print(f"Health Risk: {health_risk}")

print("========================")
