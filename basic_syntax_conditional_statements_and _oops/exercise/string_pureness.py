number = int(input())

for current_number in range(number):
    text = input()
    is_pure_sting = True
    for i in text:
        if i in(".",",","_"):
            print(f'{text} is not pure!')
            is_pure_sting = False
            break
    if is_pure_sting:
        print(f"{text} is pure.")