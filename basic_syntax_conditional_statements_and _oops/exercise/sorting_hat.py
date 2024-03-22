
wellcome_condtition = True

while wellcome_condtition:
    name = input()
    if name == 'Welcome!':
        wellcome_condtition = False
        print("Welcome to Hogwarts.")
        break
    if name == "Voldemort":
        print("You must not speak of that name! ")
        break
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")


