# after completing my complex impl of part 2 I noticed that it can be done way simpler :) not as efficiently but still good

import math

with open("input.txt", encoding='utf-8') as file:
    my_data = file.read().split("\n")

counter = 50
match = 0

for elem in my_data:
    direction = elem[0]
    amount = int(elem[1:])
    factor = 1 if direction == "R" else -1

    for _ in range(amount):
        counter = (counter + factor) % 100
        if counter == 0:
            match += 1;


print("match:",match)