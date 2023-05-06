import sys
import collections

n = int(sys.stdin.readline().rstrip())

files = []
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    tmp = collections.deque()
    tmp.extend(s)
    files.append(tmp)

result = []
for i in range(len(files[0])):
    flag = True
    before = files[0].popleft()
    for j in range(1, len(files)):
        now = files[j].popleft()
        if now != before:
            flag = False
    if flag:
        result.append(before)
    else:
        result.append("?")

print(''.join(result))