import sys

n, m = map(int, sys.stdin.readline().split())
if n == 1:
    print(1)
    sys.exit()

def first_order(train, x):
    if train[x - 1]:
        return train
    train[x - 1] = True
    return train

def second_order(train, x):
    if not train[x - 1]:
        return train
    train[x - 1] = False
    return train

def third_order(train: list):
    train.pop()
    train.insert(0, False)
    return train

def fourth_order(train: list):
    del train[0]
    train.append(False)
    return train

orders = []
for _ in range(m):
    orders.append(list(map(int, sys.stdin.readline().split())))

trains = [[False for _ in range(20)] for _ in range(n)]



for order in orders:
    if order[0] == 1:
        trains[order[1] - 1] = first_order(trains[order[1] - 1], order[2])
    elif order[0] == 2:
        trains[order[1] - 1] = second_order(trains[order[1] - 1], order[2])
    elif order[0] == 3:
        trains[order[1] - 1] = third_order(trains[order[1] - 1])
    elif order[0] == 4:
        trains[order[1] - 1] = fourth_order(trains[order[1] - 1])


result = []
for t in trains:
    if t not in result:
        result.append(t)
print(len(result))
