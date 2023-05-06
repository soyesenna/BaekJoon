import sys
import collections

_, p = map(int, sys.stdin.readline().split())

s = sys.stdin.readline().rstrip()

#deq = collections.deque()

#deq.extend(s)

condition = {'A':0, 'C':0, 'G':0, 'T':0}

con_list = list(map(int, sys.stdin.readline().split()))

condition['A'] = con_list[0]
condition['C'] = con_list[1]
condition['G'] = con_list[2]
condition['T'] = con_list[3]

cnt = 0

for i in range(len(s)-p+1):
    tmp = s[i:i+p]
    deq = collections.deque()
    deq.extend(tmp)
    counter = collections.Counter(deq)
    counter_key = counter.keys()
    flag = True
    for key in condition:
        if key not in counter_key and condition[key] > 0:
            flag = False
            break
        if condition[key] > counter[key]:
            flag = False
            break
    if flag:
        cnt += 1
print(cnt)