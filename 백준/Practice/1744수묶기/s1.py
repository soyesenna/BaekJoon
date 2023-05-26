import sys


input = sys.stdin.readline

n = int(input())

li = [int(input()) for _ in range(n)]

if n == 1:
    print(li[0])
    sys.exit()

zeros = list(filter(lambda x: x == 0, li))
minus = list(filter(lambda x: x < 0, li))
plus = list(filter(lambda x: x > 0, li))

plus.sort()

result = []
while plus:
    a = plus.pop()
    if len(plus) != 0:
        b = plus.pop()
        if a + b <= a * b:
            result.append(a*b)
        else:
            result.append(a+b)
    else:
        result.append(a)

minus.sort(reverse=True)
while minus:
    a = minus.pop()
    if len(minus) != 0:
        b = minus.pop()
        result.append(a*b)
    else:
        if len(zeros) == 0:
            result.append(a)
    
print(sum(result))