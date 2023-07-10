import sys

input = sys.stdin.readline


def in_range(a, b):
    if 0 <= a <= 18 and 0 <= b <= 18:
        return True
    return False


li = [list(map(int, input().split())) for _ in range(19)]

direction = [[0, 1], [1, 0], [1, 1], [1, -1]]

for i in range(19):
    for j in range(19):
        if li[i][j] != 0:
            for dir in direction:
                for k in range(1, 5):
                    if in_range(i + (dir[0] * k), j + (dir[1] * k)):
                        if li[i][j] != li[i + (dir[0] * k)][j + (dir[1] * k)]:
                            break
                        if k == 4:
                            print(li[i][j])
                            print(i + (dir[0] * 2) + 1, j + (dir[1] * 2) + 1)
                            sys.exit()

print(0)