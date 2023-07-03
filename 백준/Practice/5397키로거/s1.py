import sys
import collections

n = int(sys.stdin.readline())

result = []
for i in range(n):
    s = sys.stdin.readline().rstrip()
    deq = collections.deque()
    deq.extend(s)
    cursur = 0

    tmp = []
    while len(deq) != 0:
        char = deq.popleft()

        cur_len = len(tmp)
        if char == '<':
            if cursur > 0:
                cursur -= 1
        elif char == '>':
            if cursur < cur_len:
                cursur += 1
        elif char == '-':
            if cur_len != 0 and cursur != 0:
                del tmp[cursur - 1]
                cursur -= 1
        else:
            tmp.insert(cursur, char)
            cursur += 1
    
    result.append(tmp)

for s in result:
    print(''.join(s))