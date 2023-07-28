def football_points(win, draw, lost):
    total_points = 3 * win + draw + 0 * lost
    return total_points


print(football_points(3, 4, 2))
