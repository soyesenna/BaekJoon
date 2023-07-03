n, m = map(int, input().split())

#time out시 먼저 바꿔보기
chess_infer = [[
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'] 
],[
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
]
]

chess = []
for i in range(n):
    chess_col = input()
    chess_col_list = []
    for j in range(len(chess_col)):
        chess_col_list.append(chess_col[j])
    chess.append(chess_col_list)

cnt = []
i = 0
for i in range(n-7):
    for j in range(m-7):
        cnt1 = 0
        cnt2 = 0
        for k in range(8):
            for l in range(8):
                #print(chess[i+k][j+m], i,j,k,m)
                if chess[i+k][j+l] != chess_infer[0][k][l]:
                    cnt1 += 1
                if chess[i+k][j+l] != chess_infer[1][k][l]:
                    cnt2 += 1
        cnt.append(cnt1)
        cnt.append(cnt2)
print(min(cnt))