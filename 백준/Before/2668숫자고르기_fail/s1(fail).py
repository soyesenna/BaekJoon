n = int(input())

num = []
for i in range(n):
    a = int(input())
    tmp = []
    tmp.append(i+1)
    tmp.append(a)
    tmp.sort()
    num.append(tmp)

print(num)
result_list = []
for i in range(len(num)):
    if num[i][0] == num[i][1]:
        result_list.append(num[i])

FLAG = True
i = 0
while FLAG:
    if len(num) > 1:
        if num[0] in num[1:]:
            result_list.append(num[0])
            num.remove(num[0])
        else:
            num.remove(num[0])
    else:
        FLAG = False

result_list = sum(result_list, [])
result_set = set(result_list)
result_list = list(result_set)
print(len(result_list))
for i in range(len(result_list)):
    print(result_list[i])