import sys

input = sys.stdin.readline

n = int(input())

li = list(map(int, input().split()))

hol = len(list(filter(lambda x: x % 2 != 0, li)))
jjak = len(list(filter(lambda x: x % 2 == 0, li)))

result = 0
if jjak >= hol:
    result = hol
else:
    result = jjak
    flag = True
    while hol > 0:
        if flag:
            hol -= 2
            flag = False
            result += 1
        else:
            hol -= 1
            flag = True
            result += 1
    if hol < 0:
        result -= 2

print(result)