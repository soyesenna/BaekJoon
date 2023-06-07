import sys
import collections

input = sys.stdin.readline

s = list(input().rstrip())

max_num = []
min_num = []

tmp = collections.deque(s)
before = []

while tmp:
    now = tmp.popleft()
    if now == 'K':
        if len(before) == 0:
            min_num.append('5')
        else:
            min_num.append(str(10 ** (len(before)-1)))
            before = []
            min_num.append('5')
    else:
        before.append("M")

if len(before) != 0:
    min_num.append(str(10 ** (len(before) - 1)))

tmp = collections.deque(s)
before = []

while tmp:
    now = tmp.popleft()
    if now == 'K':
        if len(before) == 0:
            max_num.append('5')
        else:
            max_num.append(str(5 * 10 ** (len(before))))
            before = []
    else:
        before.append("M")

for i in range(len(before)):
    max_num.append("1")

print(''.join(max_num))
print(''.join(min_num))