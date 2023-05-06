from calendar import c
import sys
import collections

n = int(sys.stdin.readline())

a = []
result = []
cnt = 0
for i in range(n):
    tmp = int(sys.stdin.readline())
    if i+1 == tmp:
        cnt += 1
        result.append(str(tmp))
        continue
    
    tmp_list = [str(i+1), str(tmp)]
    tmp_list.sort()
    a.append(' '.join(tmp_list))

counter = collections.Counter(a)

print(counter)
for key in counter:
    if counter[key] == 2:
        cnt += 2
        for i in key.split():
            result.append(i)

result.sort()
print(cnt)
for res in result:
    print(res)

