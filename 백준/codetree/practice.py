import sys
input = sys.stdin.readline
S = input()
T = input()
ptr = -1
S = S[:-1]
T = T[:-1]
while (len(S) < len(T)):
    if T[-1] == 'A':
        if ptr > 0:
            T = T[1 :]
        else:
            T = T[: -1]
    elif T[-1] == 'B':
        if ptr > 0:
            T = T[1 :]
        else:
            T = T[: -1]
        ptr *= -1
        print("hi")
    print(T, ptr)
if ptr > 0:
    T = "".join(reversed(T))
if S == T:
    print(1)
else:
    print(0)