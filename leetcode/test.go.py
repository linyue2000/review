# coding=utf-8
import random

if __name__ == '__main__':
    n = 7
    sum, amount = 0, 0
    for i in xrange(0, 10000):
        a = random.randint(0, n)
        b = random.randint(0, n)
        sum += a ^ b
        amount += 1
    print float(sum) / float(amount)

