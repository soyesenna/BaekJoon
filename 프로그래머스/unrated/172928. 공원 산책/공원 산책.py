def solution(park, routes):
    answer = []
    for i in range(len(park)):
        if len(answer) != 0:
            break
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                answer.append(i)
                answer.append(j)
                break
    
    for route in routes:
        head, num = route.split()
        num = int(num)
        flag = True
        if head == 'E':
            if answer[1] + num > len(park[0]) - 1:
                continue
            for i in range(1, num + 1):
                if park[answer[0]][answer[1] + i] == 'X':
                    flag = False
                    break
            if flag:
                answer[1] += num
        elif head == 'W':
            if answer[1] - num < 0:
                continue
            for i in range(1, num + 1):
                if park[answer[0]][answer[1] - i] == 'X':
                    flag = False
                    break
            if flag:
                answer[1] -= num
        elif head == 'N':
            if answer[0] - num < 0:
                continue
            for i in range(1, num + 1):
                if park[answer[0]- i][answer[1]] == 'X':
                    flag = False
                    break
            if flag:
                answer[0] -= num
        else:
            if answer[0] + num > len(park) - 1:
                continue
            for i in range(1, num + 1):
                if park[answer[0]+ i][answer[1]] == 'X':
                    flag = False
                    break
            if flag:
                answer[0] += num
        
    return answer