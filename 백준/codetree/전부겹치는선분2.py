import sys

input = sys.stdin.readline

n = int(input())

li = [list(map(int, input().split())) for _ in range(n)]

mapping = [0 for _ in range(101)]

for elem in li:
    for i in range(elem[0], elem[1] + 1):
        mapping[i] += 1

if n - 1 in mapping:
    print("Yes")
else:
    print("No")