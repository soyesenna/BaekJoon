import sys

n = int(sys.stdin.readline())

li = list(sys.stdin.readline().split())

if n == 1:
    print(-1)
    sys.exit()
s1 = ''.join(li)
li[-1], li[-2] = li[-2], li[-1]

s2 = ''.join(li)

if int(s1) > int(s2):
    for i in li:
        print(i, end=' ')
else:
    print(-1)