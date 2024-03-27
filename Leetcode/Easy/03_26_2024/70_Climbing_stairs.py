def climb_stairs(n):
    stair_count = {1: 1, 2: 2}
    for i in range(3, n + 1):
        stair_count[i] = stair_count[i - 1] + stair_count[i - 2]

    return stair_count[n]


print(climb_stairs(5))
