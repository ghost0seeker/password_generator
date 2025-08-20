# Define password structure
    # upper lowerx7 upper 4xdigits 3xspecial

import os
import sys
import string
import random

upper = list(string.ascii_uppercase)
lower = list(string.ascii_lowercase)
special = ['!', '@', '#', '&', '%', '$', '*', '+', '=', '?']
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def select_function(array, seed):
    rng = random.Random(seed)
    return rng.choice(array)

def read_urandom(num_bytes):
    with open("/dev/urandom", 'rb') as f:
        return int.from_bytes(f.read(num_bytes), 'big')
        # print(int.from_bytes(f.read(num_bytes), 'big'))

def pass_gen(num_bytes):

    password = []
    password.append(select_function(upper, read_urandom(num_bytes)))
    for idx in range(7):
        password.append(select_function(lower, read_urandom(num_bytes)))
    password.append(select_function(upper, read_urandom(num_bytes)))
    for idx in range(4):
        password.append(str(select_function(digits, read_urandom(num_bytes))))
    for idx in range(3):
        password.append(select_function(special, read_urandom(num_bytes)))

    print(''.join(password))
    

if __name__ == '__main__':

    num_bytes = 10

    if len(sys.argv) > 1:
        num_bytes = int(sys.argv[1])

    pass_gen(num_bytes)
    
