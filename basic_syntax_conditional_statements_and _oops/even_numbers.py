# Get the total number of inputs to be received
n = int(input())

# Loop through each input and check for odd numbers
for i in range(n):
  number = int(input())


  if not number % 2 == 0:  # If the number is not divisible by 2 (odd)

    print(f"{number} is odd!")
    break

else:
  print("All numbers are even.")
