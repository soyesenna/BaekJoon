import sys


def is_same(king, stone):
    if king == stone:
        return True
    return False


king_s, stone_s, n = sys.stdin.readline().rstrip().split()
n = int(n)

king = [ord(king_s[0]) - 65, int(king_s[1]) - 1]
stone = [ord(stone_s[0]) - 65, int(stone_s[1]) - 1]

for _ in range(n):
    move = sys.stdin.readline().rstrip()
    if move == 'R':
        if king[0] + 1 < 8:
            king[0] += 1
            if is_same(king, stone):
                stone[0] += 1
                if stone[0] > 8:
                    stone[0] -= 1
                    king[0] -= 1
    elif move == 'L':
        if king[0] - 1 > -1:
            king[0] -= 1
            if is_same(king, stone):
                stone[0] -= 1
                if stone[0] < -1:
                    stone[0] += 1
                    king[0] += 1
    elif move == 'B':
        if king[1] + 1 < 8:
            king[1] += 1
            if is_same(king, stone):
                stone[1] += 1
                if stone[1] > 8:
                    stone[1] -= 1
                    king[1] -= 1
    elif move == 'T':
        if king[1] - 1 > -1:
            king[1] -= 1
            if is_same(king, stone):
                stone[1] -= 1
                if stone[1] < -1:
                    stone[1] += 1
                    king[1] += 1
    elif move == 'RT':
        if king[0] + 1 < 8 and king[1] - 1 > -1:
            king[0] += 1
            king[1] -= 1
            if is_same(king, stone):
                stone[0] += 1
                stone[1] -= 1
                if stone[0] > 8 or stone[1] < 0:
                    king[0] -= 1
                    stone[0] -= 1
                    king[1] += 1
                    stone[1] += 1
    elif move == 'LT':
        if king[0] - 1 > -1 and king[1] - 1 > -1:
            king[0] -= 1
            king[1] -= 1
            if is_same(king, stone):
                stone[0] -= 1
                stone[1] -= 1
                if stone[0] < 0 or stone[1] < 0:
                    king[0] -= 1
                    stone[0] -= 1
                    king[1] += 1
                    stone[1] += 1