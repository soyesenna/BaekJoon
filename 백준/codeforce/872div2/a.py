import sys

def solution(string):
  start=0
  end=len(string)-1

  while start<end:
    if string[start]!=string[end]:
      return len(string)
    start+=1
    end-=1
  end=len(string)-2
  start = 0
  while start<end:
    if string[start]!=string[end]:
      return len(string)-1
    start+=1
    end-=1
  return -1


n = int(sys.stdin.readline())
for _ in range(n):
    string=sys.stdin.readline().rstrip()
    print(solution(string))