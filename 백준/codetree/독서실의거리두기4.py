import sys


def remove_suffix_prefix(li: list):
    for i in range(len(li)):
        if li[i] != '0':
            break
        del li[0]
    for i in range(len(li) - 1, -1, -1):
        if li[i] != '0':
            break
        li.pop()
    return li


input = sys.stdin.readline

n = int(input())

li = list(input().rstrip())

result = []

for i in range(n):
    tmp = li[::]
    if tmp[i] != '1':
        tmp[i] = '1'
        for j in range(i + 1, n):
            if tmp[j] != '1':
                tmp[j] = '1'
                tmp = remove_suffix_prefix(tmp)
                tmp = ''.join(tmp)
                if '11' in tmp:
                    result.append(1)
                    tmp = list(tmp)
                    tmp[j] = '0'
                    continue
                else:
                    tmp = tmp.split('1')
                    result.append(min(map(lambda x: len(x), tmp)))
                tmp = list(tmp)
                tmp[j] = '0'

print(max(result))
