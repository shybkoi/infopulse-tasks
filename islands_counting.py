# -*- coding: utf-8 -*-

u"""Count amount of islands at the map"""

__author__ = "Shybkoi"


def mark_island(mas, x, y):
    if mas[x][y] == 1:
        mas[x][y] = 2
    if x > 0 and mas[x-1][y] == 1:
        mark_island(mas, x-1, y)
    if y > 0 and mas[x][y-1] == 1:
        mark_island(mas, x, y-1)
    if x < len(mas[0])-1 and mas[x+1][y] == 1:
        mark_island(mas, x+1, y)
    if y < len(mas)-1 and mas[x][y+1] == 1:
        mark_island(mas, x, y+1)
    return


def count_islands(mas):
    island_count = 0
    for i, k in enumerate(mas):
        while 1 == 1:
            try:
                mark_island(mas, i, k.index(1))
                island_count += 1
            except ValueError:
                break
    return island_count


if __name__ == '__main__':
    map_ = [[0, 1, 0, 0, 1, 0],
            [1, 1, 1, 0, 1, 1],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 0],
            [1, 1, 0, 0, 0, 0]]
    print('Initial map array:')
    print('\n'.join(map(str, map_)))
    print("Total islands count at the map is {}".format(count_islands(map_[:])))