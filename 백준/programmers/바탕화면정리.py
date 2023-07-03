def solution(wallpaper):

    max_c = -1
    max_r = -1
    min_c = len(wallpaper[0])
    min_r = len(wallpaper)
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                min_c = min(j, min_c)
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0]) - 1, -1, -1):
            if wallpaper[i][j] == '#':
                max_c = max(j, max_c)
                break
    
    for i in range(len(wallpaper[0])):
        for j in range(len(wallpaper)):
            if wallpaper[j][i] == '#':
                min_r = min(min_r, j)
                break
    
    for i in range(len(wallpaper[0])):
        for j in range(len(wallpaper) - 1, -1, -1):
            if wallpaper[j][i] == '#':
                max_r = max(max_r, j)
                break
    
    answer = [min_r, min_c, max_r + 1, max_c + 1]

    
    return answer

print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))