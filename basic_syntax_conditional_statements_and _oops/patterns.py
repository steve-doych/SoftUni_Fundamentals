# Get the number of rows for the pattern (largest number of stars)
number = int(input())

# Print the upper triangle (increasing number of stars)
for i in range(1, number + 1):
  # Loop for each star in a row (i represents the number of stars in this row)
  for j in range(0, i):
    # Print a star with 'end=""' to print stars on the same line
    print('*', end="")
  # Move to the next line after each row
  print()

# Print the lower triangle (decreasing number of stars)
for i in range(number-1, 0, -1):
  # Loop for each star in a row (i represents the number of stars in this row)
  for j in range(0, i):
    # Print a star with 'end=""' to print stars on the same line
    print("*", end="")
  # Move to the next line after each row
  print()
