import sys

input = sys.stdin.readline

li = list(map(int, input().split()))

li.sort()

now = li[0] - 1
while True:
    now += 1

    for i in range(5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                if now % li[i] == 0 and now % li[j] == 0 and now % li[k] == 0:
                    print(now)
                    sys.exit()
