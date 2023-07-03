def solution(players, callings):
    player_map_to_score = {}
    player_map_to_name = {}
    for i in range(len(players)):
        player_map_to_score[i + 1] = players[i]
        player_map_to_name[players[i]] = i + 1
    for call in callings:
        now_score = player_map_to_name[call]
        before_player = player_map_to_score[now_score - 1]
        
        player_map_to_name[call] -= 1
        player_map_to_name[before_player] += 1
        player_map_to_score[now_score] = before_player
        player_map_to_score[now_score - 1] = call
        
    answer = sorted(list(player_map_to_name.items()), key=lambda x: x[1])
    answer = list(map(lambda x: x[0], answer))
    
    
    return answer



print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))