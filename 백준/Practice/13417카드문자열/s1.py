import sys
import collections

t = int(sys.stdin.readline())

for _ in range(t):
    _ = sys.stdin.readline()

    card = list(sys.stdin.readline().rstrip().split())
    deq = collections.deque()
    deq.extend(card)
    card = collections.deque()
    while deq:
        a = deq.popleft()
        if len(card) == 0:
            card.append(a)
        else:
            b = card.popleft()
            if b >= a:
                card.appendleft(b)
                card.appendleft(a)
            else:
                card.appendleft(b)
                card.append(a)
    while card:
        print(card.popleft(), end='')
    print('')