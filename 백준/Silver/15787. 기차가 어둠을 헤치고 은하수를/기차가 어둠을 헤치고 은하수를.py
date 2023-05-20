n, m = map(int, input().split())
train = [[0]*20 for _ in range(n)]
for _ in range(m):
    order = list(map(int, input().split()))
    if order[0]==1:    #승차
        train[order[1]-1][order[2]-1] = 1

    elif order[0]==2:  #하차
        train[order[1]-1][order[2]-1] = 0

    elif order[0]==3:  #한 칸씩 뒤로
        for i in range(19,0,-1):
            train[order[1]-1][i] = train[order[1]-1][i-1]
        train[order[1]-1][0] = 0

    else:           #한 칸씩 앞으로
        for i in range(19):
            train[order[1]-1][i] = train[order[1]-1][i+1]
        train[order[1]-1][19] = 0

result = []
for t in train:
    if t not in result:
        result.append(t)
print(len(result))