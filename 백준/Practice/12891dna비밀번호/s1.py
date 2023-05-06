import sys
import collections

s, p = map(int, sys.stdin.readline().split())

dna = sys.stdin.readline().rstrip()
num_list = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0
for i in range(len(dna)-p+1):
    now = dna[i:p+i]
    counter = collections.Counter(now)

    if counter['A'] >= num_list[0] and counter['C'] >= num_list[1] and counter['G'] >= num_list[2] and counter['T'] >= num_list[3]:
        cnt += 1

print(cnt)