import sys

n, m = map(int, sys.stdin.readline().split())

s = []
for _ in range(n):
    s.append(sys.stdin.readline().rstrip())

cnt= 0
for _ in range(m):
    q = sys.stdin.readline().rstrip()

    for j in range(len(s)):
        if q == s[j][:len(q)]:
            cnt += 1
            break
print(cnt)