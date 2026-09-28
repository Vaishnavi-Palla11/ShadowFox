import random

six_count = 0
one_count = 0
two_sixes = 0
previous_roll = 0

for i in range(20):
    roll = random.randint(1, 6)
    print("Roll", i+1, ":", roll)

    if roll == 6:
        six_count += 1
    if roll == 1:
        one_count += 1
    if roll == 6 and previous_roll == 6:
        two_sixes += 1
    previous_roll = roll

print("Number of times rolles 6: ", six_count)
print("Number of times rolled 1: ", one_count)
print("Number of times rolled two 6s in a row: ", two_sixes)       

