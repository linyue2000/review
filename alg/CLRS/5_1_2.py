# coding=utf-8
import random
import time
import math


def random_0_1():
    return random.randint(0, 1)


def random_a_b(a, b):
    if a > b:
        return 0
    elif a == b:
        return a
    c = b - a
    num_digits = 0 if c == 0 else int(math.log(c, 2)) + 1
    while True:
        result = 0
        for i in xrange(0, num_digits):
            digit = random_0_1()
            result = result * 2 + digit
        if result <= c:
            return a + result


if __name__ == '__main__':
    random.seed(time.time())
    a, b = 1, 9
    for i in xrange(0, 10):
        for j in xrange(0, 100):
            print random_a_b(a, b),
        print
