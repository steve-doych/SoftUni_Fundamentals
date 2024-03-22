number_of_messages = int(input())

for current_message in range(number_of_messages):
    number_input = int(input())
    if number_input == 88:
        print("Hello")
    elif number_input == 86:
        print("How are you?")
    elif number_input < 88:
        print("GREAT!")
    elif number_input > 88:
        print("Bye.")
        