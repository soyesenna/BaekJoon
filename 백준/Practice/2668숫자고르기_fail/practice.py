import sys

n = int(sys.stdin.readline())

result = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    if a == b:
        result.append("YES")
        continue
    if a < b:
        result.append("NO")
        continue

    i = 1
    flag = False
    while a % 3 == 0:
        a /= 3
        tmp = a

        for j in range(i + 1):
            if tmp == b:
                result.append("YES")
                flag = True
                break 
            tmp *= 2
        if flag:
            break
        i += 1
        
    if not flag:
        result.append("NO")

for res in result:
    print(res)