import sys

n = int(sys.stdin.readline())

mapping = []

for _ in range(n):
    for a in list(map(int, sys.stdin.readline().split())):
        mapping.append(a)
    mapping.sort(reverse=True)
    mapping.pop()


#mapping.sort()
print(mapping[n-1])