import os
import sys
import string
import random
import secrets

NUM_BYTE = 32

UPPER = list(string.ascii_uppercase)
LOWER = list(string.ascii_lowercase)
SPECIAL = ['!', '@', '#', '&', '%', '$', '*', '+', '=', '?']
DIGIT = [str(digit) for digit in range(0,10)]


def read_urandom():
    with open("/dev/urandom", "rb") as f:
        return int.from_bytes(f.read(NUM_BYTE), 'big')


def select_char(array, seed):
   return random.Random(seed).choice(array)


def passgen():

    password = []
    
    def build_pass(CHARSET, seed):
        password.append(select_char(CHARSET, seed))

    build_pass(UPPER, read_urandom())
    for _ in range(7):
        build_pass(LOWER, read_urandom())
    build_pass(UPPER, read_urandom())
    for _ in range(4):
        build_pass(DIGIT, read_urandom())
    for _ in range(3):
        build_pass(SPECIAL, read_urandom())
    
    return ''.join(password)

if __name__ == "__main__":
    # TODO: Make passgen of flexible length based on user input
    print(passgen())