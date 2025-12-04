# efficient but not as readable - for a more readable solution check part-2-alt.py

import math

with open("input.txt", encoding='utf-8') as file:
    my_data = file.read().split("\n")

count = 50
division_count = 0
match_count = 0

for elem in my_data:
    direction = elem[0]
    amount = int(elem[1:])
    factor = 1 if direction == "R" else -1

    currentDivCounter = math.floor((count + amount * factor) / 100)
    match_count += abs(division_count - currentDivCounter)
    division_count = currentDivCounter

    if direction == "L" and (count + amount * factor) % 100 == 0:
        match_count += 1
    if direction == "L" and count % 100 == 0:
        match_count -= 1

    count += amount * factor


print("match:", match_count)