from itertools import combinations

def choose(n,k):
    if k == 0: 
       return 1
    elif n < k:
       return 0
    else:
        return choose(n-1, k-1) + choose(n-1, k)
    
n = int(input())

num_dict = {}
for i in range(n):
    a = int(input())
    num_dict[i+1] = a

select_num = n
FLAG = True

while FLAG:
    subset_num = 0
    for subset_num in range(choose(n, select_num)):
        select_first_list = list(combinations(num_dict.keys(), select_num))[subset_num]
        tmp_list = []
        for j in range(len(select_first_list)):
            tmp_list.append(num_dict[select_first_list[j]])
        tmp_tuple = tuple(tmp_list)
        if tmp_tuple == select_first_list:
            FLAG = False
            print(len(tmp_tuple))
            for k in range(len(tmp_tuple)):
                print(tmp_tuple[k])
            
    select_num -= 1

