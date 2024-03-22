#This program reads floating-point numbers until a number between 1 and 100 (inclusive) is entered.

# Loop continuously until a valid number is found
while True:
  number = float(input())

  # Check if the number is between 1 and 100 (inclusive)
  if 1 <= number <= 100:
    # Print a message with the valid number
    print(f"The number {number} is between 1 and 100")
    # Exit the loop after finding a number within the range
    break