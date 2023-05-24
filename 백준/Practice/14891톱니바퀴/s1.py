import sys
import collections

input = sys.stdin.readline

li = []
for _ in range(4):
    deq = collections.deque()
    deq.extend(map(lambda x: int(x), input().rstrip()))
    li.append(deq)

k = int(input())

def rotate_right(num, dir):
    global li
    if num == 3:
        #dir true : 시계
        #dir false : 반시계
        if dir:
            li[num].appendleft(li[num].pop())
        else:
            li[num].append(li[num].popleft())
        return
    
    if li[num][2] != li[num+1][6]:
        rotate_right(num+1, not dir)

    if dir:
        li[num].appendleft(li[num].pop())
    else:
        li[num].append(li[num].popleft())
    
    return

def rotate_left(num, dir):
    global li
    if num == 0:
        if dir:
            li[num].appendleft(li[num].pop())
        else:
            li[num].append(li[num].popleft())
        return

    if li[num][6] != li[num-1][2]:
        rotate_left(num-1, not dir)
    if dir:
        li[num].appendleft(li[num].pop())
    else:
        li[num].append(li[num].popleft())
    return


for _ in range(k):
    #톱니번호, 방향
    #dir 1 : 시계
    #dir 2 : 반시계 
    num, dir = map(int, input().split())

    num -= 1

    if dir == 1:
        rotate_right(num, True)
        li[num].append(li[num].popleft())
        rotate_left(num, True)
    else:
        rotate_right(num, False)
        li[num].appendleft(li[num].pop())
        rotate_left(num, False)


result = 0
for i in range(4):
    result += (li[i].popleft()) * (2 ** i)
print(result)