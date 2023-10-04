#!/usr/bin/python3
# loop through the ASCII values of lowercase letter
print("".join([
    "abcdefghijklmnopqrstuvwxyz"[i] \
    for i in range(len("abcdefghijklmnopqrstuvwxyz")) if i != 16 and i != 24
]))

