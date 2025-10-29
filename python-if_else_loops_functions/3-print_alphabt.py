#!/usr/bin/python3
#ptyhon script that prints the ASCII alphabet followed by new line
for i in range(97, 123):
    if i != 101 and i != 113:
        print("{}".format(chr(i)), end="")
