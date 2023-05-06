n = int(input())
xy_list = []
for i in range(n):
    a, b = map(int, input().split(' '))
    xy_list.append([a,b])

res_list = []
for i in range(n):
    cnt = 0
    for j in range(n):
        if xy_list[i][0] < xy_list[j][0] and xy_list[i][1] < xy_list[j][1]:
            cnt += 1
    res_list.append(cnt)

for i in res_list:
    print(i + 1, end=' ')
