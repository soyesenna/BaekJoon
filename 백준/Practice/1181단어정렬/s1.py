import sys

n = int(sys.stdin.readline())

words = set()

for _ in range(n):
    words.add(sys.stdin.readline().rstrip())

words_list = sorted(list(words), key=lambda x: (len(x), x))


for word in words_list:
    print(word)