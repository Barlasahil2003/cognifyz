# Temperature Conversion Program

# Prompt the user to enter a temperature value
temperature = float(input("Enter the temperature value: "))

# Prompt the user to enter the unit of measurement (C or F)
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()

# Check the unit and perform the conversion
if unit == "C":
    # Convert Celsius to Fahrenheit
    fahrenheit = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {fahrenheit:.2f}°F")
elif unit == "F":
    # Convert Fahrenheit to Celsius
    celsius = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {celsius:.2f}°C")
else:
    # Handle invalid input
    print("Invalid unit. Please enter 'C' or 'F'.")
