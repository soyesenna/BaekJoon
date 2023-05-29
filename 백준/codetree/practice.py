import sys
import collections

input = sys.stdin.readline

n = int(input())

persons = [list(input().split()) for _ in range(n)]

li = ['' for _ in range(max(map(lambda x: int(x[0]), persons)))]

for person in persons:
    li[int(person[0])-1] = person[1]

for i in range(len(li) - 1, -1, -1):
    for j in range(len(li) - i):
        if li[j+i] == '' or li[j] == '':
            continue
        counter = collections.Counter(li[j:j+i+1])
        keys = list(counter.keys())
        try:
            del keys[keys.index('')]
        except:
            pass
        if len(keys) == 1:
            print(i)
            sys.exit()
        else:
            if counter['G'] == counter['H']:
                print(i)
                sys.exit()
