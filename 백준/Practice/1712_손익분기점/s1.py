a, b, c = map(int, input().split())

if b < c:
    cnt = a // (c - b)
    while True:
        gen_num = a + (b * cnt)
        profit_num = c * cnt
        if gen_num < profit_num:
            break
        cnt += 1
        #print(gen_num, profit_num)

    print(cnt)
else:
    print(-1)

    