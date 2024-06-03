import random

def gen_pass(pass_length):
    elements = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLPNOPQRSTUVWXYZ1234567890+-/*!&$#?=@<>"
    password = ""

    for i in range(int(pass_length)):
        password += random.choice(elements)

    return password

