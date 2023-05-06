import sys

n = (sys.stdin.readline().rstrip())[:-2]
f = int(sys.stdin.readline())

result = 0
for i in range(100):
    if i // 10 == 0:
        i = '0' + str(i)
    else:
        i = str(i)
    
    a = int(n + i)

    if a % f == 0:
        result = str(a)
        break
print(result[-2:])