import sys
import collections

n, m = map(int, sys.stdin.readline().split())

to_n = set()

for i in range(n):
    to_n.add(sys.stdin.readline().rstrip())

to_m = set()
to_count_m = []
for i in range(m):
    tmp = sys.stdin.readline().rstrip()
    to_m.add(tmp)
    to_count_m.append(tmp)

m_counter = collections.Counter(to_count_m)
result = to_n & to_m

cnt = 0
for s in result:
    cnt += m_counter[s]
    
print(cnt)