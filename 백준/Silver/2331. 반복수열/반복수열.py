import sys

a, p = map(int, sys.stdin.readline().split())

li = [a]

while True:
    tmp = str(li[-1])
    tmp_n = 0
    for i in range(len(tmp)):
        tmp_n += int(tmp[i]) ** p
    if tmp_n not in li:
        li.append(tmp_n)
    else:
        li = li[:li.index(tmp_n)]
        break

print(len(li))