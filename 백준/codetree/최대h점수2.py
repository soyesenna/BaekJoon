import sys

input = sys.stdin.readline

n, l = map(int, input().split())

li = list(map(int, input().split()))

predict = max(li) + 1

while predict >= 0:
    a = list(filter(lambda x: x >= predict, li))
    if len(a) >= predict:
        print(predict)
        sys.exit()
    a = list(filter(lambda x: x >= predict - 1, li))
    if len(a) >= predict:
        b = list(filter(lambda x: x == predict - 1, li))
        if len(b) <= l:
            print(predict)
            sys.exit()
    predict -= 1