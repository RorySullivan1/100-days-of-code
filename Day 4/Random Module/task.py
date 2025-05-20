import random

rand_num = random.randint(1, 10)

rand_float_0_1 = random.random()
rand_float_range = random.uniform(1,10)

def flip_coin():
    num = random.randint(0,1)
    if num == 0:
        val = "Heads"
    else:
        val = "Tails"
    print(val)

flip_coin()