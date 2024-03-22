# Get the initial budget from the user as an integer
budget = int(input())
command = input()
price = 0

while command != "End":
    price = int(command)
    budget -= price
    if budget < 0:
        print("You went in overdraft!")
        break
    command = input()
else:
    print("You bought everything needed.")

