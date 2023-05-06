#이진탐색

import sys

n = int(sys.stdin.readline())

n_map = sys.stdin.readline().split()


m = int(sys.stdin.readline())

m_list = sys.stdin.readline().split()

for i in range(m):
    head = 0
    mid = len(n_map) // 2
    tail = len(n_map) - 1
    while True:
        if m_list[i] > n_map[mid]:
            head = mid
        elif m_list[i] < n_map[mid]:
            tail = mid
        elif m_list[i] == n_map[mid]:
            print(1)
            break
        mid = (tail + head) // 2

        if mid == head and head == tail:
            print(0)
            break
        

13579