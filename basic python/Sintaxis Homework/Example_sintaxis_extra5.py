celsius_temp = float (input("Enter the temperature you want to convert: "))
fahrenheit_temp = (celsius_temp * 1.8) + 32
kelvin_temp = celsius_temp + 273.15

print(f"Fahrenheit: {fahrenheit_temp}")
print(f"Kelvin: {kelvin_temp}")