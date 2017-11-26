# coding=utf-8
import sys


def left_index(i):
    return i * 2 + 1


def right_index(i):
    return i * 2 + 2


def parent_index(i):
    return (i - 1) / 2


def shift_down(list, i):
    while True:
        il = left_index(i)
        ir = right_index(i)
        min = sys.maxint
        min_index = None
        if il < len(list):
            l = list[il]
            if ir < len(list):
                r = list[ir]
                if l < r:
                    min = l
                    min_index = il
                else:
                    min = r
                    min_index = ir
            else:
                min = l
                min_index = il
        if min_index is None or list[i] <= min:
            break
        list[i], list[min_index] = list[min_index], list[i]
        i = min_index


def shift_up(list, i):
    while i > 0:
        ip = parent_index(i)
        if list[ip] > list[i]:
            list[ip], list[i] = list[i], list[ip]
            i = ip
        else:
            break


def create_heap(list):
    for i in xrange(parent_index(len(list) - 1), -1, -1):
        shift_down(list, i)


def insert(list, n):
    list.append(n)
    shift_up(list, len(list) - 1)


def pop(list):
    if len(list) == 0:
        return
    list[0] = list[len(list) - 1]
    list.pop()
    shift_down(list, 0)


def get(list):
    if len(list) == 0:
        return None
    return list[0]


if __name__ == '__main__':
    list = [9, 3, 7, 6, 5, 1, 10, 2]
    create_heap(list)
    print list
    n = get(list)
    pop(list)
    while n is not None:
        print n, list
        n = get(list)
        pop(list)
