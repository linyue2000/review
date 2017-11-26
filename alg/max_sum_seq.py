# coding=utf-8

def normal(list):
    sum = 0
    s = 0
    e = 0
    for i in xrange(0, len(list)):
        sum_test = 0
        for j in xrange(i, len(list)):
            sum_test += list[j]
            if sum_test > sum:
                sum = sum_test
                s = i
                e = j
    return s, e, sum


def fastest(list):
    sum = 0
    s = 0
    e = 0
    sum_test = 0
    s_test = 0
    for i in xrange(0, len(list)):
        sum_test += list[i]
        if sum_test > sum:
            sum = sum_test
            s = s_test
            e = i
        elif sum_test < 0:
            sum_test = 0
            s_test = i + 1
    return s, e, sum


if __name__ == '__main__':
    list = [-8, 3, 6, 9, -6, 10, -16, 18, 11]
    print normal(list)
    print fastest(list)
