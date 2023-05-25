from enum import Flag
import sys
import collections

#flag true : R
#flag false : C
def sorting(li: list, flag):
    max_len = 0
    for i in range(len(li)):
        counter = [list(e) for e in collections.Counter(li[i]).items()]
        counter.sort(key=lambda x: (x[1], x[0]))
        counter = list(filter(lambda x: x[0] != 0, counter))
        tmp_li = [item for sublist in counter for item in sublist]
        li[i] = tmp_li
        max_len = max(max_len, len(li[i]))
    for i in range(len(li)):
        li[i].extend([0 for _ in range(max_len - len(li[i]))])
        if len(li[i]) >= 100:
            li[i] = li[i][:100]
    if flag:
        return li
    else:
        li.reverse()
        return li

input = sys.stdin.readline

r,c,k = map(int, input().split())

li = [list(map(int, input().split())) for _ in range(3)]

time = 0
while time <= 100:
    if 0 <= r-1 < len(li) and 0 <= c-1 < len(li[0]) and li[r-1][c-1] == k:
        print(time)
        sys.exit()
    time += 1
    if len(li) >= len(li[0]):
        li = sorting(li, True)
    else:
        li = sorting([list(e) for e in zip(*li)], False)
        li = [list(e) for e in zip(*li[::-1])]

print(-1)

