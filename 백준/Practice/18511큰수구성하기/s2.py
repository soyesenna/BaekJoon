import sys

n, k = sys.stdin.readline().split()
li = list(map(int, sys.stdin.readline().split()))
li.sort(reverse=True)
flag = False
result = ''
for i in range(len(n)):
    if flag:
        result += str(max(li))
        continue
    if int(n[i]) in li:
        result += n[i]
    else:
        for j in li:
            if j <= int(n[i]):
                result += str(j)
                flag = True
                break

if len(result) == len(n):
    print(result)
    sys.exit()

result = str(li[0]) + str(li[0])
print(result)            