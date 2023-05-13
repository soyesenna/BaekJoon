import sys
import collections

def get_hamming(s1, s2):
    cnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt += 1
    return cnt

n, m = map(int, sys.stdin.readline().split())

dna = []
for _ in range(n):
    dna.append(sys.stdin.readline().rstrip())

count = []
for i in range(m):
    tmp = []
    for j in range(n):
        tmp.append(dna[j][i])
    count.append(tmp)

result = ''
for i in range(m):
    counter = collections.Counter(count[i])#.most_common()
    if len(collections.Counter(list(counter.values())).values()) == 1:
        counter = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    else:
        counter = counter.most_common()
        #("A", 4), ("B", 3)
    #print(counter)
    result += counter[0][0]

result_len = 0
for i in range(n):
    result_len += get_hamming(result, dna[i])
print(result)
print(result_len)