import sys
import collections
n, k = map(int, sys.stdin.readline().split())

num_list = []
for i in range(1, n+1):
    num_list.append(i)

i = -1
factor = len(num_list)
result = []
while len(num_list) != 0:
    i += k
    if factor != 0:
        if i // factor >= 1:
            for j in range(len(result) - 1, -1, -1):
                if result[j] in num_list:
                    num_list.remove(result[j])
                else:
                    break
            i %= factor
            factor = len(num_list)
            if factor == 0:
                break
            if i // factor >= 1:
                i %= factor
            result.append(num_list[i])   
        else:
            i %= factor
            result.append(num_list[i])

s = '<'
for i in range(len(result)):
    s += str(result[i]) + ',' + ' '

re_s = s[: -2]
re_s += '>'
print(re_s)
