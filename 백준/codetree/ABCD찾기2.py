import sys

input = sys.stdin.readline

li = sorted(list(map(int, input().split())))

for i in range(1, 15):
    for j in range(1, 15):
        for k in range(1, 15):
            for r in range(1, 15):
                tmp = sorted([i, j, k, r, i + j, i + k, i + r, j + k, j + r, k + r, i + j + k, i + j + r, j + k + r, i + k + r, i + j + k + r])
                if tmp == li:
                    print(i, j, k, r)
                    sys.exit()