import sys

input = sys.stdin.readline

t, a, b = map(int, input().split())

points = [list(input().split()) for _ in range(t)]

s = list(map(lambda x: int(x[1]), (filter(lambda x: x[0] == 'S', points))))
n = list(map(lambda x: int(x[1]), (filter(lambda x: x[0] == 'N', points))))

cnt = 0
for i in range(a, b + 1):
    s_min = min(map(lambda x: abs(x - i), s))
    n_min = min(map(lambda x: abs(x - i), n))
    if s_min <= n_min:
        cnt += 1
print(cnt)