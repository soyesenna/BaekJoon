import sys

chess = [[True, False, True, False, True, False, True, False],
        [False, True, False, True, False, True, False, True],
        [True, False, True, False, True, False, True, False],
        [False, True, False, True, False, True, False, True],
        [True, False, True, False, True, False, True, False],
        [False, True, False, True, False, True, False, True],
        [True, False, True, False, True, False, True, False],
        [False, True, False, True, False, True, False, True]
]

cnt = 0
for i in range(8):
    s = sys.stdin.readline().rstrip()
    for j in range(8):
        if s[j] == 'F' and chess[i][j]:
            cnt += 1

print(cnt)