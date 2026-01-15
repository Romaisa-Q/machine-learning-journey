# Weight input
weight = float(input("Enter your weight in kg: "))

# Height input in feet and inches
feet = int(input("Enter your height (feet): "))
inches = int(input("Enter remaining inches: "))

# Convert height to meters
total_inches = (feet * 12) + inches
height_meters = total_inches * 0.0254

# BMI calculation
bmi = weight / (height_meters ** 2)

# BMI category (WHO standards)
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Output
print("\n--- BMI Result ---")
print("Height in meters:", round(height_meters, 2))
print("Your BMI:", round(bmi, 2))
print("Category:", category)
