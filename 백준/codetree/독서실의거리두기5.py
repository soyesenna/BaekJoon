import sys

input = sys.stdin.readline

n = int(input())

li = list(input().rstrip())

result = []
for i in range(n):
    if li[i] != '1':
        tmp = li[::]
        tmp[i] = '1'
        if i == 0 and tmp[i+1] == '1':
            result.append(1)
            continue
        elif i == n-1 and tmp[i-1] == '1':
            result.append(1)
            continue
        elif 0 < i < n-1:
            if tmp[i-1] == '1' or tmp[i+1] == '1':
                result.append(1)
                continue
        for j in range(len(tmp)):
            if tmp[0] == '0':
                tmp.pop(0)
            else:
                break
        for j in range(len(tmp) - 1, -1, -1):
            if tmp[-1] == '0':
                tmp.pop()
            else:
                break
        tmp = ''.join(tmp)
        if '11' in tmp:
            result.append(1)
            continue
        tmp = tmp.split('1')
        result.append(min(map(lambda x: len(x) + 1, filter(lambda x: x != '', tmp))))

print(max(result))