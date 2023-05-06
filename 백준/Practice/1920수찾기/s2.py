
import sys
import collections

n = int(sys.stdin.readline())

n_list = sys.stdin.readline().split()
n_map = collections.Counter(n_list)
#print(n_map)

m = int(sys.stdin.readline())

m_list = sys.stdin.readline().split()

for i in range(m):
    if m_list[i] in n_map:
        print(1)
    else:
        print(0)