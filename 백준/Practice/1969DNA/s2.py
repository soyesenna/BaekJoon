import sys

N, M = map(int, sys.stdin.readline().split())
dna_list = [sys.stdin.readline().rstrip() for _ in range(N)]
result_dna = ''
hamming_distance = 0

for i in range(M):
    cnt = [0, 0, 0, 0]
    for dna in dna_list:
        if dna[i] == 'A':
            cnt[0] += 1
        elif dna[i] == 'C':
            cnt[1] += 1
        elif dna[i] == 'G':
            cnt[2] += 1
        elif dna[i] == 'T':
            cnt[3] += 1
    
    max_value = max(cnt)
    max_index = cnt.index(max_value)
    hamming_distance += (N - max_value)

    if max_index == 0:
        result_dna += 'A'
    elif max_index == 1:
        result_dna += 'C'
    elif max_index == 2:
        result_dna += 'G'
    elif max_index == 3:
        result_dna += 'T'

print(result_dna)
print(hamming_distance)
