command_string = input()

while command_string != "End":
    if command_string != "SoftUni":
        for char in command_string:
            print(char * 2, end="")
        print()
    command_string = input()
