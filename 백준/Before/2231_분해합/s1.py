n = int(input())

i = '1'
iscant = False

while True:
    if int(i) >= n:
        iscant = True
        break
    sum = int(i)
    for j in range(len(i)):
        sum += int(i[j])
    if sum == n:
        break
    tmp = int(i) + 1
    i = str(tmp)

if not iscant:
    print(int(i))
else:
    print(0)