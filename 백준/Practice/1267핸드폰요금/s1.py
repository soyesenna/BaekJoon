import sys

n = int(sys.stdin.readline())

time = list(map(int, sys.stdin.readline().split()))

result = [0,0]

for a in time:
    result[0] += ((a // 30) + 1) * 10
    result[1] += ((a // 60) + 1) * 15

if result[0] < result[1]:
    print('Y', result[0])
elif result[0] > result[1]:
    print('M', result[1])
else:
    print('Y M', result[0])