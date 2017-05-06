# -*- coding: utf-8 -*-

u"""Range function implementation"""

__author__ = "Shybkoi"


def myrange(first, final, step):
    if ((step > 0 and first > final) or
            (step < 0 and first < final)):
        raise ValueError("Incorrect input data!")

    tmp = first
    while tmp != final:
        yield tmp
        tmp += step


if __name__ == '__main__':
    for k in myrange(6, 1, -1):
        print(k)

