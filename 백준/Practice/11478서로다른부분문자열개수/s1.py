import sys
import collections

s = (sys.stdin.readline().rstrip())

deq = collections.deque(s)

tmp_to_conter = []

while len(deq) != 0:
    to_del = deq.popleft()
    tmp_to_conter.append(to_del)

    for _ in range(len(deq)):
        tmp = deq.popleft()
        tmp_list = [tmp_to_conter[-1], tmp]
        tmp_s = ''.join(tmp_list)
        tmp_to_conter.append(tmp_s)
        deq.append(tmp)
    
count = collections.Counter(tmp_to_conter)

print(len(count))