# Ask for two digits
num1 = int(input("Enter the first digit: "))
num2 = int(input("Enter the second digit: "))

# Arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulo = num1 % num2
exponent = num1 ** num2

# Display results
print("\n--- Arithmetic Operations ---")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
print(f"Floor Division: {num1} // {num2} = {floor_division}")
print(f"Modulo: {num1} % {num2} = {modulo}")
print(f"Exponent: {num1} ** {num2} = {exponent}")
