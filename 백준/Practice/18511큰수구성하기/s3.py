import sys
import itertools

n, k = sys.stdin.readline().split()
n = tuple(n)
li = list(sys.stdin.readline().split())
li.sort(reverse=True)

pro = list(itertools.product(li, repeat=len(n)))
pro.append(n)
pro.sort(reverse=True)

pro.extend(sorted(list(itertools.product(li, repeat=len(n) - 1)), reverse=True))

print(''.join(pro[pro.index(n) + 1]))

