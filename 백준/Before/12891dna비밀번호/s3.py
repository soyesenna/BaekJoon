import sys
import collections

s_len, p = map(int, sys.stdin.readline().split())

s = sys.stdin.readline().rstrip()

deq = collections.deque()
deq.extend(s)

condition = {'A':0, 'C':0, 'G':0, 'T':0}

con_list = list(map(int, sys.stdin.readline().split()))

condition['A'] = con_list[0]
condition['C'] = con_list[1]
condition['G'] = con_list[2]
condition['T'] = con_list[3]

now = collections.deque()
for _ in range(p):
    a = deq.popleft()
    now.append(a)

counter = collections.Counter(now)
condition_key = condition.keys()
cnt = 0
flag = True
for key in condition_key:
    if key not in counter.keys():
        counter[key] = 0
        if condition[key] > 0:
            flag = False
            continue
    elif counter[key] < condition[key]:
        flag = False
if flag:
    cnt += 1

for i in range(s_len - p):
    flag = True
    a = deq.popleft()
    now.append(a)
    b = now.popleft()
    counter[a] += 1
    counter[b] -= 1
    for key in condition_key:
        if counter[key] < condition[key]:
            flag = False
            break
    if flag:
        cnt += 1

print(cnt)