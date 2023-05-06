import sys
import collections

s = list(sys.stdin.readline().rstrip().split(' '))

result_type = []
result_name = []

for i in range(1, len(s)):
    tmp_type = s[0]
    deq = collections.deque(s[i])

    tmp_name = ''
    for _ in range(len(deq)):
        last = deq.popleft()
        if not('a' <= last <= 'z' or 'A' <= last <= 'Z'):
            deq.appendleft(last)
            break
        tmp_name += last
    result_name.append(tmp_name)

    for _ in range(len(deq)):
        last = deq.pop()
        if last == ',' or last == ';':
            continue
        if last == '[':
            tmp_type += ']'
        elif last == ']':
            tmp_type += '['
        else:
            tmp_type += last
    result_type.append(tmp_type)

for i in range(len(result_type)):
    print(result_type[i], result_name[i]+';')