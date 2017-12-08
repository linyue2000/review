# coding=utf-8

def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0
    d, x, y = extended_euclid(b, a % b)
    return d, y, x - (a / b) * y


if __name__ == '__main__':
    print extended_euclid(99, 78)
