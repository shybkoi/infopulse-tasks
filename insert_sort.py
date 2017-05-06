# -*- coding: utf-8 -*-

u"""Array sorting by insert algorithm."""

__author__ = "Shybkoi"


def ins_sort(m, order='asc'):
    """order may contain asc or desc value
    """
    for i in range(1, len(m)):
        for j in range(i, 0, -1):
            if ((m[j - 1] > m[j] and order == 'asc') or
                    (m[j - 1] < m[j] and order == 'desc')):
                m[j - 1], m[j] = m[j], m[j - 1]
            else:
                break


if __name__ == '__main__':
    mas = [20, 5, 7, 6.5, -0.2, 10, 3, 58]
    print('Initial array: {}'.format(mas))
    try:
        ins_sort(mas, 'asc')
        print('Sorted array: {}'.format(mas))
    except TypeError:
        print('Incorrect input array!')