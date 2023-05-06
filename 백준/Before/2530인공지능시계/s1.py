import sys

time = list(map(int, sys.stdin.readline().split()))
done = int(sys.stdin.readline())

result = [0,0,0]

result[0] = (done // 3600) + time[0]
done -=  (done // 3600) * 3600

result[1] = (done // 60) + time[1]
done -=  (done // 60) * 60

result[2] = done + time[2]

if result[2] >= 60:
    result[1] += result[2] // 60
    result[2] -= (result[2] // 60) * 60

if result[1] >= 60:
    result[0] += result[1] // 60
    result[1] -= (result[1] // 60) * 60

if result[0] >= 24:
    result[0] -= (result[0] // 24) * 24

print(result[0], result[1], result[2])