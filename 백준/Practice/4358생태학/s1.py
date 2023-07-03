import sys
import collections

s_list = []
cnt = 0
while True:
    a = sys.stdin.readline().rstrip()
    if not a:
        break
    s_list.append(a)
    cnt += 1


counter = collections.Counter(s_list)
keys = sorted(list(counter.keys()))
for key in keys:
    print("%s %.4f" %(key, (counter[key]/cnt)*100))