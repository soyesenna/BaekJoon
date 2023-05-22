def solution(name, yearning, photo):
    score = {}
    for i in range(len(name)):
        score[name[i]] = yearning[i]
    
    keys = list(score.keys())
    answer = []
    for now_photo in photo:
        tmp = 0
        for person in now_photo:
            if person in keys:
                tmp += score[person]
        answer.append(tmp)
    return answer