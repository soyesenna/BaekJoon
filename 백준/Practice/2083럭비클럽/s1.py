import sys

while True:
    s = list(sys.stdin.readline().rstrip().split())

    if s[0] == '#':
        break

    if int(s[1]) > 17 or int(s[2]) >= 80:
        print(s[0] , 'Senior')
    else:
        print(s[0] , 'Junior')

