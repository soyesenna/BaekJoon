import sys

input = sys.stdin.readline

n, b = map(int, input().split())

#가격, 배송비
present = [list(map(int, input().split())) for _ in range(n)]

#present.sort(key=lambda x: (sum(x), x[0]))

cnt = 0

for i in range(n):
    now_price = 0
    present[i][0] //= 2
    tmp = sorted(present, key=lambda x:sum(x))
    for j in range(n):
        now_price += sum(tmp[j])
        if now_price > b:
            cnt = max(cnt, j)
            break
        if j == n - 1:
            print(n)
            sys.exit()
    present[i][0] *= 2
print(cnt)