import sys
import collections

HYDRO = 1
OXY = 16
C = 12

s = (sys.stdin.readline().rstrip())
s_deq = collections.deque()
s_deq.extend(s)

buf_deq = collections.deque()#stack
#print(s_deq)
for _ in range(len(s_deq)):
    tmp = s_deq.pop()
    if tmp == 'H':
        buf_deq.appendleft(HYDRO)
    elif tmp == 'C':
        buf_deq.appendleft(C)
    elif tmp == 'O':
        buf_deq.appendleft(OXY)
    else:
        buf_deq.appendleft(tmp)

buf_cnt = 0
total_cnt = 0

while len(buf_deq) != 0:
    tmp = buf_deq.popleft()
    if tmp == '(':
        braket_buf_cnt = 0
        while tmp != ')':
            tmp = buf_deq.popleft()
            if type(tmp) == type(1):
                total_cnt += tmp
                braket_buf_cnt += tmp
                buf_cnt = tmp
            elif tmp >= '2' and tmp <= '9':
                total_cnt += buf_cnt * (int(tmp) - 1)
                braket_buf_cnt += buf_cnt * (int(tmp) - 1)
        if tmp >= '2' and tmp <= '9':
            total_cnt += braket_buf_cnt * (int(tmp) - 1)

print(total_cnt)

