import sys
import itertools

def recursion(n, li, idx, now_length=0):
    if idx == now_length:
        if n >= int(''.join(li)):
            return int(''.join(li))
        else:
            return 0
    for i in range(len(li)):
        for j in range(i, len(li)):
            li[i], li[j] = li[j], li[i]
            now = recursion(n, li, idx, now_length + 1)
            if now != 0:
                return now
            li[i], li[j] = li[j], li[i]
    return 0

    

n, k = sys.stdin.readline().split()
li = sorted(list(sys.stdin.readline().split()), reverse=True)

for coms in list(itertools.combinations_with_replacement(li, len(n))):
    for i in range(len(n), 0, -1):
        res = recursion(int(n), list(coms), i)
        if res != 0:
            print(res)
            sys.exit()
