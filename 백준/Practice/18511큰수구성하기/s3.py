import sys
import itertools
from profile import Profile
from pstats import Stats

profile = Profile()

def main():
    n, k = sys.stdin.readline().split()
    n = tuple(n)
    li = list(sys.stdin.readline().split())
    li.sort(reverse=True)

    pro = list(itertools.product(li, repeat=len(n)))
    pro.append(n)
    pro.sort(reverse=True)

    pro.extend(sorted(list(itertools.product(li, repeat=len(n) - 1)), reverse=True))

    print(''.join(pro[pro.index(n) + 1]))



if __name__ == "__main__":
    profile.run("main()")
    stats = Stats(profile)
    stats.print_stats()

    main()
