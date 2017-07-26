# -*- coding: utf-8 -*-

u""" demo linked lists with one and two relations"""

__author__ = "Shybkoi"


class NodeTypeOne:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListOneR:
    u"""linked list with one relationship"""

    def __init__(self):
        self.first = None
        self.size = 0

    def add(self, data):
        node = NodeTypeOne(data)
        self.size += 1
        if self.first is None:
            self.first = node
        else:
            temp = self.first
            while temp.next is not None:
                temp = temp.next
            temp.next = node

    def insert(self, data, index):
        if not check_index(index, self.size):
            return False
        pointer = 1
        temp = self.first
        prev = None
        while pointer < int(index):
            prev = temp
            temp = temp.next
            pointer += 1
        new_node = NodeTypeOne(data)
        new_node.next = temp
        if prev is not None:
            prev.next = new_node
        self.size += 1

    def remove(self, index):
        if not check_index(index, self.size):
            return
        pointer = 1
        temp = self.first
        prev = None
        while pointer < int(index):
            prev = temp
            temp = temp.next
            pointer += 1
        if prev is not None:
            prev.next = temp.next
        else:
            self.first = temp.next
        self.size -= 1


class NodeTypeTwo:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedListTwoR:
    u"""linked list with two relationships"""

    def __init__(self):
        self.first = None
        self.size = 0

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
        self.size += 1

    def insert(self, data, index):
        if not check_index(index, self.size):
            return False
        pointer = 1
        temp = self.first
        prev = None
        while pointer < int(index):
            prev = temp
            temp = temp.next
            pointer += 1
        new_node = NodeTypeTwo(data)
        new_node.next = temp
        temp.prev = new_node
        new_node.prev = prev
        if prev is not None:
            prev.next = new_node
        else:
            self.first = new_node
        self.size += 1

    def remove(self, index):
        if not check_index(index, self.size):
            return
        pointer = 1
        temp = self.first
        prev = None
        while pointer < int(index):
            prev = temp
            temp = temp.next
            pointer += 1
        if prev is not None:
            prev.next = temp.next
            temp.next.prev = prev
        else:
            self.first = temp.next
            temp.next.prev = None
        self.size -= 1


def check_index(index, size):
    try:
        if int(index) <= 0:
            print("Index must be natural number!")
            return False
    except ValueError:
        print("Index must be a number!")
        return False
    if int(index) > size:
        print("Index is out of range list!")
        return False
    return True


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

    sl.remove(2)
    print_list(sl)

    sl.remove(1)
    print_list(sl)

    dl = LinkedListTwoR()
    dl.add({"first": 1, "2": (1, 2)})
    dl.add("g = 9.8")
    dl.add((4, 7, 8))
    print(dl.__doc__)
    print_list(dl)

    dl.remove(2)
    print_list(dl)

    dl.insert({"insert first": "75"}, 1)
    print_list(dl)