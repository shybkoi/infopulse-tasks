# -*- coding: utf-8 -*-

u""" demo linked lists with one and two relations"""

__author__ = "Shybkoi"


class NodeTypeOne:
    def __init__(self, data):
        self.data = data
        self.next = None


class NodeTypeTwo:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedListOneR:
    u"""linked list with one relationship"""
    def __init__(self):
        self.first = None

    def add(self, data):
        node = NodeTypeOne(data)
        if self.first is None:
            self.first = node
        else:
            temp = self.first
            while temp.next is not None:
                temp = temp.next
            temp.next = node

    def insert(self, data, index):
        if not check_index(index):
            return
        i = 1
        temp = self.first
        prev = None
        while True:
            if i == int(index):
                n1 = NodeTypeOne(data)
                n1.next = temp
                if prev is not None:
                    prev.next = n1
                break
            prev = temp
            temp = temp.next
            i += 1
            if temp is None:
                break
        if int(index) > i:
            raise IndexError

    def del_node(self, index):
        if not check_index(index):
            return
        i = 1
        temp = self.first
        prev = None
        while True:
            if i == int(index):
                if prev is not None:
                    prev.next = temp.next
                elif i == 1:
                    self.first = temp.next
                del(temp)
                break
            prev = temp
            temp = temp.next
            i += 1
            if temp is None:
                break
        if int(index) > i:
            raise IndexError

    def self_show(self):
        n1 = self.first
        print(n1.data)
        while n1.next is not None:
            n1 = n1.next
            print(n1.data)


class LinkedListTwoR:
    u"""linked list with two relationships"""
    def __init__(self):
        self.first = None

    def add(self, data):
        node = NodeTypeTwo(data)
        if self.first is None:
            self.first = node
        else:
            temp = self.first
            while temp.next is not None:
                temp = temp.next
            temp.next = node
            node.prev = temp

    def self_show(self):
        n1 = self.first
        print(n1.data)
        while n1.next is not None:
            n1 = n1.next
            print(n1.data)


def check_index(index):
    try:
        if int(index) > 0:
            return True
    except ValueError:
        print("Index must be integer!")
        return False


def print_list(list_object):
    n1 = list_object.first
    print(n1.data)
    while n1.next is not None:
        n1 = n1.next
        print(n1.data)
    print("*" * 20)


if __name__ == "__main__":
    sl = LinkedListOneR()
    sl.add([1, 2])
    sl.add("data string")
    sl.add(3.14)
    print(sl.__doc__)
    print_list(sl)

    sl.insert(12, 2)
    print_list(sl)

    sl.insert("test", 3)
    print_list(sl)

    sl.insert({"final": 5}, 5)
    print_list(sl)

    sl.del_node(2)
    print_list(sl)

    sl.del_node(1)
    print_list(sl)

    dl = LinkedListTwoR()
    dl.add({"first": 1, "2": (1, 2)})
    dl.add("g = 9.8")
    dl.add((4, 7, 8))
    print(dl.__doc__)
    print_list(dl)






