def calculate_bmi(weight,height):
    return weight / (height**2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"
    
try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    
    if weight <= 0 or height <= 0:
        print("Weight and height must be positive numbers.")    
    else:
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Which is classified as: {category}")
except ValueError:
    print("Please enter valid numbers for weight and height.")