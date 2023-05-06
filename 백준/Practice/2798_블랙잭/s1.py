n, m = map(int, input().split(' '))
card = list(map(int, input().split(' ')))

minus_list = []

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and i != k and j != k:
                tmp = (card[i] + card[j] + card[k]) - m
                if tmp <= 0:
                    minus_list.append(tmp)


print(max(minus_list) + m)