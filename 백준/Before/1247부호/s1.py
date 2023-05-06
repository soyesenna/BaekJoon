import sys

for _ in range(3):
    n = int(sys.stdin.readline())

    num= []
    for _ in range(n):
        num.append(int(sys.stdin.readline()))

    a = sum(num)

    if a > 0:
        print('+')
    elif a < 0:
        print('-')
    else:
        print('0')