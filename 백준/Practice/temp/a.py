import functools

a = [1,2,3,4,5,6,7,8,9,10]

# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         print(a[i])

b = list(filter(lambda x: x % 2 == 0, a))
c = map(lambda x: , a)

print(type(c))

print(c[0])

for elem in b:
    print(elem)

