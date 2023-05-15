import sys

def recursion(s, l, r, cnt=1):
    if l >= r:
        return 1, cnt
    elif s[l] != s[r]:
        return 0, cnt
    else:
        return recursion(s, l + 1, r - 1, cnt+1)

def is_penrildrome(s):
    return recursion(s, 0, len(s) - 1)

n = int(sys.stdin.readline())
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    isp, cnt = is_penrildrome(s)
    print(isp, cnt)