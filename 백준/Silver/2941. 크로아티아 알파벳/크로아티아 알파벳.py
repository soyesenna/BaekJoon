import sys

s = sys.stdin.readline().rstrip()

croateia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for cro in croateia:
    if cro in s:
        #s = ''.join(s.split(cro))
        s = s.replace(cro, '@')

print(len(s))