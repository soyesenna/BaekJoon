import sys
import collections

n = int(sys.stdin.readline())

score = {'1':0, '2':0}
win_time = {'1':0, '2':0}
now_flag = ['d', 0]

for _ in range(n):
    team, time = sys.stdin.readline().rstrip().split()

    time = time.split(':')
    time = (int(time[0][0]) * 600) + (int(time[0][1]) * 60) + int(time[1])
    #print(time)
    score[team] += 1
    
    if now_flag[0] == 'd':
        now_flag[0] = team
        now_flag[1] = time
    elif now_flag[0] == '1' and team == '2':
        if score['1'] == score['2']:
            now_flag[0] = 'd'
            win_time['1'] += time - now_flag[1]
    elif now_flag[0] == '2' and team == '1':
        if score['1'] == score['2']:
            now_flag[0] = 'd'
            win_time['2'] += time - now_flag[1]

if now_flag[0] != 'd':
    if now_flag[0] == '1':
        win_time['1'] += 2880 - now_flag[1]
    else:
        win_time['2'] += 2880 - now_flag[1]

for i in range(1,3):
    min = win_time[str(i)] // 60
    sec = win_time[str(i)] - (min * 60)

    if len(str(min)) < 2:
        min = '0' + str(min)
    if len(str(sec)) < 2:
        sec = '0' + str(sec)
    print("{0}:{1}".format(min,sec))

