#!/usr/bin/python3
for letter in range(97, 123):
    if chr(letter) is not 'q' and chr(letter) is not 'e':
        print("{}".format(chr(letter)), end="")
# loop through the ASCII values of lowercase letters
for char in range(ord('a'), ord('z') + 1):
    if char != ord('e') and char != ord('q'):
        print(chr(char), end=" ")
