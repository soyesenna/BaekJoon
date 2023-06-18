import sys

input = sys.stdin.readline

n, m = map(int, input().split())

li = list(map(int, input().split()))

predict = 1

while predict < sum(li):
    tmp = li[::]
    section = [[] for _ in range(m)]
    now_section = 0
    flag = True
    while len(tmp) != 0:
        now = tmp.pop()
        if now > predict:
            flag = False
            break
        if now + sum(section[now_section]) <= predict:
            section[now_section].append(now)
        else:
            now_section += 1
            if now_section == m:
                flag = False
                break
            else:
                section[now_section].append(now)
    if flag:
        print(predict)
        break
    predict += 1