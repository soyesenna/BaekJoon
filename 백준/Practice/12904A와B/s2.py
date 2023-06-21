import sys

input = sys.stdin.readline

origin = list(input().rstrip())
target = list(input().rstrip())

while len(origin) < len(target):
    if target[-1] == 'A':
        target.pop()
    else:
        target.pop()
        target.reverse()

if origin == target:
    print(1)
else:
    print(0)