# Get a floating-point number from the user as input
number = float(input())

# Check if the number is exactly zero
if number == 0:
  print("zero")
# Otherwise, check if the number is positive
elif number > 0:
  # Check if the absolute value of the number is less than 1
  if abs(number) < 1:
    print("small positive")
  # Check if the absolute value of the number is greater than 1 million
  elif abs(number) > 1000000:
    print("large positive")
  # Otherwise the number is positive but not small or large
  else:
    print("positive")
# Otherwise the number is negative
else:
  # Check if the absolute value of the number is less than 1
  if abs(number) < 1:
    print("small negative")
  # Check if the absolute value of the number is greater than 1 million
  elif abs(number) > 1000000:
    print("large negative")
  # Otherwise, the number is negative but not small or large
  else:
    print("negative")
