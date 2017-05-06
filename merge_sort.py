# -*- coding: utf-8 -*-

u"""Array sorting by merge algorithm."""

__author__ = "Shybkoi"


def merge(mas1, mas2):
    buf1 = 0
    buf2 = 0
    i = 0
    maxl = len(mas1) + len(mas2)
    res = []
    while i < maxl:
        if mas1[buf1] < mas2[buf2]:
            res.append(mas1[buf1])
            buf1 += 1
        else:
            res.append(mas2[buf2])
            buf2 += 1
        if buf1 == len(mas1):
            res += mas2[buf2:]
            break
        elif buf2 == len(mas2):
            res += mas1[buf1:]
            break
        i += 1
    return res

def sort_mas(mas):
    if len(mas) <= 1:
        return mas
    half = int(len(mas)/2)
    mas1 = sort_mas(mas[:half])
    mas2 = sort_mas(mas[half:])
    return merge(mas1, mas2)


if __name__ == '__main__':
    mas = [12, 5, -7, 6.5, 0.2, 8, 3]
    print('Initial array: {}'.format(mas))
    try:
        print('Sorted array: {}'.format(sort_mas(mas)))
    except TypeError:
        print('Incorrect input array!')
