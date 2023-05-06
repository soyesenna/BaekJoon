import sys

t = int((sys.stdin.readline().rstrip()))

for _ in range(t):

    a, b = sys.stdin.readline().rstrip().split()

    a = a[-1]
    if a == '0':
        print(10)
    else:
        b = int(b) % 4
        if b == 0:
            b = 4
        n = str(int(a) ** int(b))
        print(n)
        print(n[-1])

