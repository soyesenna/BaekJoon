H, W = map(int, input().split())
blocks = list(map(int, input().split()))

# 각 위치에서 왼쪽의 최대 높이를 계산
left_maxes = [0] * W
left_max = 0
for i in range(W):
    left_max = max(left_max, blocks[i])
    left_maxes[i] = left_max

# 각 위치에서 오른쪽의 최대 높이를 계산
right_maxes = [0] * W
right_max = 0
for i in range(W-1, -1, -1):
    right_max = max(right_max, blocks[i])
    right_maxes[i] = right_max

# 각 위치에서 고일 수 있는 빗물의 양을 계산
water = 0
for i in range(W):
    water += min(left_maxes[i], right_maxes[i]) - blocks[i]

print(water)
