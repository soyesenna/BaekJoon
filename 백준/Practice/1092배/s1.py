import sys

input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))

m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if cranes[0] < boxes[0]:
    print(-1)
    sys.exit()

cnt = 0
while boxes:
    for i in range(n):
        for j in range(len(boxes)):
            if boxes[j] <= cranes[i]:
                del boxes[j]
                if len(boxes) == 0:
                    cnt += 1
                    print(cnt)
                    sys.exit()
                break

    cnt += 1
print(cnt)

