import sys
T = int(sys.stdin.readline())
for _ in range(T):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, sys.stdin.readline().split())
    dist = ((x_1 - x_2)**2 + (y_1 - y_2)**2)**0.5
    if x_1 == x_2 and y_1 == y_2 and r_1 == r_2:
        print(-1)
    elif r_1 + r_2 == dist or abs(r_1 - r_2) == dist:
        print(1)
    elif r_1 + r_2 > dist and dist > abs(r_1 - r_2):
        print(2)
    else:
        print(0)