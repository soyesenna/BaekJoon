n = int(input())

for i in range(n):
    vps = input()
    stack = []
    for j in range(len(vps)):
        stack.append(vps[j])
        if len(stack) >= 2:
            if stack[-1] == ')' and stack[-2] == '(':
                stack.pop()
                stack.pop()
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")

    