import sys

input = sys.stdin.readline

n = int(input())

li = [input().rstrip().split() for _ in range(n)]

mapping = [0 for _ in range(2001)]

now_idx = 1000
#mapping[now_idx] += 1
for dir in li:
    if dir[1] == 'R':
        for i in range(int(dir[0])):
            now_idx += 1
            mapping[now_idx] += 1
    else:
        for i in range(int(dir[0])):
            now_idx -= 1
            mapping[now_idx] += 1

cnt = 0
for i in range(len(mapping)):
    if mapping[i] > 1:
        cnt += 1

print(cnt)
