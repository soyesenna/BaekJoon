import sys
import collections

#시작, 끝, 스트리밍끝
s, e, q = (map(float, sys.stdin.readline().rstrip().replace(':', '.').split()))

times = []
names = []
check_start = set()
check_end = set()
while True:
    tmp = sys.stdin.readline().rstrip()
    if not tmp:
        break
    time, name = tmp.split()
    time = float(time.replace(':', "."))
    times.append(time)
    names.append(name)


for i in range(len(times)):
    if times[i] <= s:
        check_start.add(names[i])
    elif e <= times[i] <= q:
        check_end.add(names[i])

cnt = len(check_start & check_end)
print(cnt)
