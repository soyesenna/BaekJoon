import sys


def is_same(king, stone):
    if king == stone:
        return True
    return False


def right(king, stone):
    if king[0] + 1 > 8:
        return king, stone, False
    else:
        king[0] += 1
        if is_same(king, stone):
            stone[0] += 1
            if stone[0] > 8:
                stone[0] -= 1
                king[0] -= 1
                return king, stone, False
    return king, stone, True


def left(king, stone):
    if king[0] - 1 < 1:
        return king, stone, False
    else:
        king[0] -= 1
        if is_same(king, stone):
            stone[0] -= 1
            if stone[0] < 1:
                stone[0] += 1
                king[0]+= 1
                return king, stone, False
    return king, stone, True


def up(king, stone):
    if king[1] + 1 > 8:
        return king, stone, False
    else:
        king[1] += 1
        if is_same(king, stone):
            stone[1] += 1
            if stone[1] > 8:
                king[1] -= 1
                stone[1] -= 1
                return king, stone, False
    return king, stone, True


def down(king, stone):
    if king[1] - 1 < 1:
        return king, stone, False
    else:
        king[1] -= 1
        if is_same(king, stone):
            stone[1] -= 1
            if stone[1] < 1:
                king[1] += 1
                stone[1] += 1
                return king, stone, False
    return king, stone, True


def rightup(king, stone):
    if king[0] + 1 > 8 or king[1] + 1>  8:
        return king, stone
    else:
        king[0] += 1
        king[1] += 1
        if is_same(king, stone):
            stone[0] += 1
            stone[1] += 1
            if stone[0] > 8 or stone[1] > 8:
                stone[0] -= 1
                stone[1] -= 1
                king[0] -= 1
                king[1] -= 1
    return king, stone


def leftup(king, stone):
    if king[0] - 1 < 1 or king[1] + 1 > 8:
        return king, stone
    else:
        king[0] -= 1
        king[1] += 1
        if is_same(king, stone):
            stone[0] -= 1
            stone[1] += 1
            if stone[0] < 1 or stone[1] > 8:
                stone[0] += 1
                stone[1] -= 1
                king[0] += 1
                king[1] -= 1
    return king, stone

    return king, stone


def rightdown(king, stone):
    if king[0] + 1 > 8 or king[1] - 1 < 1:
        return king, stone
    else:
        king[0] += 1
        king[1] -= 1
        if is_same(king, stone):
            stone[0] += 1
            stone[1] -= 1
            if stone[0] > 8 or stone[1] < 1:
                stone[0] -= 1
                stone[1] += 1
                king[0] -= 1
                king[1] += 1
    return king, stone


def leftdown(king, stone):
    if king[0] - 1 < 1 or king[1] - 1 < 1:
        return king, stone
    else:
        king[0] -= 1
        king[1] -= 1
        if is_same(king, stone):
            stone[0] -= 1
            stone[1] -= 1
            if stone[0] < 1 or stone[1] < 1:
                stone[0] += 1
                stone[1] += 1
                king[0] += 1
                king[1] += 1
    return king, stone


king_s, stone_s, n = sys.stdin.readline().rstrip().split()
n = int(n)

king = [ord(king_s[0]) - 65 + 1, int(king_s[1])]
stone = [ord(stone_s[0]) - 65 + 1, int(stone_s[1])]

for _ in range(n):
    move = sys.stdin.readline().rstrip()
    if move == 'R':
        king, stone, _ = right(king, stone)
    elif move == 'L':
        king, stone, _ = left(king, stone)
    elif move == 'B':
        king, stone, _ = down(king, stone)
    elif move == 'T':
        king, stone, _ = up(king, stone)
    elif move == 'RT':
        king, stone = rightup(king, stone)
    elif move == 'LT':
        king, stone = leftup(king, stone)
    elif move == 'RB':
        king, stone = rightdown(king, stone)
    elif move == 'LB':
        king, stone = leftdown(king, stone)

king_res = chr(king[0] + 64) + str(king[1])
stone_res = chr(stone[0] + 64) + str(stone[1])
print(king_res)
print(stone_res)




