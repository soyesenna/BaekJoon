from re import L
import sys

while True:
    n = (sys.stdin.readline().rstrip())

    if n == '0':
        break

    length = 2 + (len(n) - 1)
    for i in range(len(n)):
        if n[i] == '1':
            length += 2
        elif n[i] == '0':
            length += 4
        else:
            length += 3
    
    print(length)