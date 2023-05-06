a = int(input())
res = []

for i in range(a):
    cnt = 0
    n ,m= map(int, input().split())
    k = list(map(int, input().split(' ')))
    '''
    tmp_list = []
    for j in range(len(k)):
        if j == m:
            tmp_list.append('key')
        else:
            tmp_list.append(str(j))
    dict_ = dict(zip(tmp_list, k))
    print(dict_.pop(0))
    '''
    tmp_list = []
    for j in range(len(k)):
        if j == m:
            tmp_list.append('key')
        else:
            tmp_list.append(str(j))
    
    while True:
        tmp = k.pop(0)
        tmp2 = tmp_list.pop(0)
        if len(k) == 0:
            cnt += 1
            break
        if max(k) <= tmp:
            cnt += 1
            if tmp2 == 'key':
                break
        else:
            k.append(tmp)
            tmp_list.append(tmp2)
        
    res.append(cnt)

for i in range(len(res)):
    print(res[i])