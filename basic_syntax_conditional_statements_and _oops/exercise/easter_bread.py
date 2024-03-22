budget = float(input())
price_one_kg_flour = float(input())
price_for_pack_eggs = price_one_kg_flour * 0.75
price_for_kg_milk = price_one_kg_flour + 1.25

price_per_loaf = price_one_kg_flour + price_for_pack_eggs + price_for_kg_milk /4
loaf_counter = 0
coloured_eggs_counter = 0

while True:
    if price_per_loaf > 0:
        break
    budget -= price_per_loaf
    loaf_counter += 1
    coloured_eggs_counter += 3
    if loaf_counter     % 3 == 0:
        coloured_eggs_counter -= loaf_counter - 2
print(f"You made {loaf_counter} loaves of Easter bread! Now you have {coloured_eggs_counter} \
eggs and {budget:.2f}BGN left.")