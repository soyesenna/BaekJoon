import sys
import collections
from unittest import result

deq = collections.deque((sys.stdin.readline().rstrip()))

result_deq = collections.deque()
while len(deq) != 0:
    char = deq.popleft()

    if char == '<':
        result_deq.appendleft(char)
        while char != '>':
            char = deq.popleft()
            result_deq.appendleft(char)
        if len(deq) != 0:
            tmp_word = []
            char = deq.popleft()
            tmp_word.append(char)
            while char == ' ':
                char = deq.popleft()
        else:
            break


