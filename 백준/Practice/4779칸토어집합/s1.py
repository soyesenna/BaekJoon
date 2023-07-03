import sys

def recursion(n):
    if n == 1:
        return '-'
    return recursion(n // 3) + " " * (n // 3) + recursion(n // 3)

while True:
    try:
        n = int(sys.stdin.readline())
        if n == 0:
            print('-')
            continue

        print(recursion(3 ** n))
    except:
        break
