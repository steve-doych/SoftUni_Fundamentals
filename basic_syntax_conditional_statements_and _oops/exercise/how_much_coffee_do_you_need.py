"""while command != "End":
    current_command = input()
    if current_command == "coding" or current_command == "dog" or current_command == "cat" or \
            current_command == "movie":
        coffee_counter += 1
    elif current_command == 'CODING' or current_command == "DOG" or current_command == "CAT" or \
            current_command == 'MOVIE':
        coffee_counter += 2

    elif current_command == "SoftUni":
        continue
    if coffee_counter > 5:
        print("You need extra sleep")
        break
    current_command = input()
"""
command = input()
coffee_counter = 0
list_of_events = ["coding", "dog", "cat","moive"]
list_of_events_upp = ["CODING", 'DOG',"CAT","MOVIE"]
while command != 'END':

    if command in list_of_events:
        coffee_counter +=1
    elif command in list_of_events_upp:
        coffee_counter +=2
    command = input()
    if command =="END":
        if coffee_counter > 5:
            print("You need extra sleep")
        else:
            print(coffee_counter)



