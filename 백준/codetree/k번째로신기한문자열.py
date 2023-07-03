n, k, t = input().split()

s_li = []
for _ in range(int(n)):
    s_li.append(input())

res = []
for s in s_li:
    if s[:len(t)] == t:
        res.append(s)

res.sort()

print(res[int(k) - 1])