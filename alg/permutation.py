# coding=utf-8

def p(list, offset):
    if offset == len(list):
        if offset > 0:
            print_list(list)
        return
    else:
        for i in xrange(offset, len(list)):
            list[offset], list[i] = list[i], list[offset]
            p(list, offset + 1)
            list[offset], list[i] = list[i], list[offset]


def print_list(list):
    for n in list:
        print n,
    print


if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    p(list, 0)
