# -*- coding: utf-8 -*-

"""Stop iteration demo"""

__author__ = "Shybkoi"


def my_gen(num):
    i = 0
    while i < num:
        yield i
        i += 1

if __name__ == "__main__":
    f = my_gen(10)
    while True:
        try:
            print(next(f))
        except StopIteration:
            print("End of generator!")
            break
