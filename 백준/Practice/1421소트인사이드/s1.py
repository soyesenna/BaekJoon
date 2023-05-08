import sys

s = sys.stdin.readline().rstrip()

li = []
for i in range(len(s)):
    li.append(s[i])


li.sort(reverse=True)

for n in li:
    print(n, end='')