#!/usr/bin/python3
# loop through the ASCII values of lowercase letters
for char in range(ord('a'), ord('z') + 1):
    if char != ord('e') and char != ord('q'):
        print(chr(char), end=" ")
