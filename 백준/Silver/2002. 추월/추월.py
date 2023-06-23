n=int(input())
arr1=[input() for _ in range(n)] 
arr2=[input() for _ in range(n)]
cnt=0
for i in range(len(arr1)):
    a=False
    for j in range(0,i):
        if arr2.index(arr1[j])>arr2.index(arr1[i]):
            a=True
    if a:
        cnt+=1
print(cnt)