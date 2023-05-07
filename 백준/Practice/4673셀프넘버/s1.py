n = 1

num_list = []
while n <= 10000:
    tmp = str(n)
    tmp_l = [int(tmp)]

    for i in range(len(tmp)):
        tmp_l.append(int(tmp[i]))
    num_list.append(sum(tmp_l))
    n += 1

for i in range(1, 10001):
    if i not in num_list:
        print(i)
