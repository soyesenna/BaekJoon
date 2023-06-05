import sys

input = sys.stdin.readline

n, k = map(int, input().split())

li = list(map(int, input().split()))

for i in range(max(li), 0, -1):
    jump = 0
    for elem in li:
        if elem > i:
            jump += 1
        else:
            jump = 0
        if jump > k - 1:
            print(i + 1)
            sys.exit()
print(max(li))