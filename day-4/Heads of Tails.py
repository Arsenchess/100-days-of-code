import random

random_integer = random.randint(0, 1)
if random_integer == 1:
    random_integer = "Heads"
    print(random_integer)
else:
    random_integer = "Tails"
    print(random_integer)
