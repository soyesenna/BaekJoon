import sys
import collections

input = sys.stdin.readline

n, k = map(int, input().split())

con = collections.deque(map(lambda x: [int(x), False], input().split()))
num_zero = 0
cnt = 0

while num_zero < k:
    cnt += 1
    head = con.pop()
    con.appendleft(head)
    con[n-1][1] = False
    for i in range(len(con) - 1, -1, -1):
        now_robot = con[i]
        if now_robot[1]:
            to_move = i + 1
            if to_move == 2 * n:
                to_move = 0
            move_robot = con[to_move]
            if not move_robot[1] and move_robot[0] > 0:
                now_robot[1] = False
                move_robot[1] = True
                move_robot[0] -= 1
                if move_robot[0] == 0:
                    num_zero += 1
                if to_move == n -1:
                    move_robot[1] = False
    if con[0][0] > 0:
        con[0][1] = True
        con[0][0] -= 1
        if con[0][0] == 0:
            num_zero += 1

print(cnt)
    