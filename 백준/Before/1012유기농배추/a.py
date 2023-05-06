a = []

for i in range(5):
    tmp = [1 for j in range(5)]
    a.append(tmp)

for i in range(5):
    if 1 in a[i]:
        print(a[i].index(1))