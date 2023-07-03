import sys
import collections

def to_bool(n):
    if n == '1':
        return True
    return False

def penrildrom(switch):
    deq = collections.deque(switch)

    while len(deq) != 1:
        left = deq.popleft()
        right = deq.pop()
        if left != right:
            return False
    
    return True


def male(switch, number):
    for i in range(number - 1, len(switch), number):
        switch[i] = not switch[i]
    return switch

def female(switch, number):
    max_len = min(len(switch) - number - 1, number)
    left_idx = number - max_len
    right_idx = number + max_len
    pen_flag = True
    while pen_flag:
        pen_flag = not penrildrom(switch[left_idx:right_idx + 1])
        left_idx += 1
        right_idx -= 1

    left_idx -= 1
    right_idx += 1
    for i in range(left_idx, right_idx + 1):
        switch[i] = not switch[i]
    return switch

n = int(sys.stdin.readline())

switch = list(map(lambda x: to_bool(x), sys.stdin.readline().split()))

t = int(sys.stdin.readline())

students = []
for _ in range(t):
    tmp = list(map(int, sys.stdin.readline().split()))
    students.append([tmp[0], tmp[1] - 1])

for i in range(t):
    if students[i][0] == 1:
        switch = male(switch, students[i][1] + 1)
    else:
        switch = female(switch, students[i][1])

for i in range(len(switch)):
    if i % 20 == 0 and i != 0:
        print()
    if switch[i]:
        print(1, end=' ')
    else:
        print(0, end=' ')