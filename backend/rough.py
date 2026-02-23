import os
import sys
import string
import random

upper = list(string.ascii_uppercase)
lower = list(string.ascii_lowercase)
special = ['!', '@', '#', '&', '%', '$', '*', '+', '=', '?']
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if __name__ == "__main__":

    with open("/dev/urandom", "rb") as f:
        seed1 = int.from_bytes(f.read(32), "big")
    
    with open("/dev/urandom", "rb") as f:
        seed2 = int.from_bytes(f.read(32), "big")
    
    rng1 = random.Random(seed1)
    rng2 = random.Random(seed2)

    result1 = rng1.choice(upper)
    result2 = rng2.choice(upper)

    x = 1