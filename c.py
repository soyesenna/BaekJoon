N = int(input())

routes = [input().split() for _ in range(N)]
remaining_cities = []

for i in range(1, N + 1):
    for country in ['A', 'B', 'C']:
        city = country + str(i)
        if city not in [route[0] for route in routes] and city not in [route[1] for route in routes]:
            remaining_cities.append(city)

for route in routes:
    start, end = route
    print(start, end='', ' ')
    if start[0] == end[0]:
        print(remaining_cities.pop(), end='', ' ')
        if remaining_cities and remaining_cities[-1][0] != start[0]:
            print(remaining_cities.pop(), end='', ' ')
    elif remaining_cities and remaining_cities[-1][0] != start[0] and remaining_cities[-1][0] != end[0]:
        print(remaining_cities.pop(), end='', ' ')
    print(end)
