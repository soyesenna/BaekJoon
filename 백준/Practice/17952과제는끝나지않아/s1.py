import sys


def do_work(li):
    if li[-1][2] == 1:
        li[-1][2] -= 1
        return li[-1][1]
    li[-1][2] -= 1
    return 0

n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))

scroe = 0
now = []
for i in range(n):
    if li[i] != [0]:
        now.append(li[i])
        scroe += do_work(now)
        if now[-1][2] == 0:
            now.pop()
        continue
    else:
        if len(now) != 0:
            scroe += do_work(now)
            if now[-1][2] == 0:
                now.pop()
            continue
print(scroe)
