import sys
import collections

n, score, p = map(int, sys.stdin.readline().split())
if n == 0:
    li = []
else:
    li = list(map(int, sys.stdin.readline().split()))

li.sort(reverse=True)

if n != 0 and score <= li[-1]:
    if len(li) == p:
        print(-1)
        sys.exit()

li.append(score)

counter = collections.Counter(li)
keys = sorted(list(counter.keys()), reverse=True)
result = 0
for key in keys:
    if key == score:
        result += 1
        break
    else:
        result += counter[key]
print(result)