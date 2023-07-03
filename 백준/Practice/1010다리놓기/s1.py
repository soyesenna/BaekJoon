def factorial(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result

def combination(m, n):
    result = 1
    for i in range(n):
        result *= m
        m -= 1
    result = result / factorial(n)
    return int(result)

t = int(input())

result = []

for i in range(t):
    n ,m= map(int, input().split())
    c = combination(m,n)
    result.append(c)

for i in range(len(result)):
    print(result[i])