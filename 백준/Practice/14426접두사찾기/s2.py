import sys

def solve(li, target):
    for s in li:
        if s[0:len(target)] == target:
            return True
    return False

n, m = map(int, sys.stdin.readline().split())

s = []
for _ in range(n):
    s.append(sys.stdin.readline().rstrip())

pro = []
for _ in range(m):
    pro.append(sys.stdin.readline().rstrip())

cnt = 0
for i in range(len(pro)):
    if solve(s, pro[i]):
        cnt += 1

print(cnt)