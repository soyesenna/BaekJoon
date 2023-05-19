import sys
import itertools

def check(li, per_li):

    res = [0 for _ in range(len(per_li))]

    for i in range(len(per_li) - 1, -1, -1):
        for j in range(i, -1, -1):
            if per_li[i] < per_li[j]:
                res[per_li[i] - 1] += 1
    
    return res == li


def main():
    n = int(sys.stdin.readline())
    li = list(map(int, sys.stdin.readline().split()))

    per = list(itertools.permutations([i for i in range(1, n + 1)], n))


    for per_li in per:
        if check(li, per_li):
            for i in per_li:
                print(i, end=' ')
            break

main()