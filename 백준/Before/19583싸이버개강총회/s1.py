import sys
import collections

#시작, 끝, 스트리밍끝
s, e, q = (map(float, sys.stdin.readline().rstrip().replace(':', '.').split()))

times = []
names = []
while True:
    tmp = sys.stdin.readline().rstrip()
    if not tmp:
        break
    time, name = tmp.split()
    time = float(time.replace(':', "."))
    times.append(time)
    names.append(name)

cor_start_time = 0
for time in times:
    if time <= s:
        cor_start_time += 1
    else:
        break

cor_e = None
cor_q = None
for i in range(cor_start_time, len(times), 1):
    if times[i] <= q and times[i] >= e:
        if cor_e ==  None:
            cor_e = i
    else:
        cor_q = i - 1
        break


cor_start_student = names[:cor_start_time]
cor_end_student = names[cor_e:cor_q]

to_count = cor_start_student + cor_end_student
counter = collections.Counter(to_count)

result = 0
for key in counter:
    if counter[key] > 1:
        result += 1
print(result)
