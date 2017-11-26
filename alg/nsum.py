# coding=utf-8

#找出offset开始的n个数，和为sum
def p(list, offset, n, sum):
    if n > len(list) - offset:
        return False, []
    if n == 0:
        if sum == 0:
            return True, []
        else:
            return False, []

    result, indices = p(list, offset + 1, n - 1, sum - list[offset])
    if result:
        indices.append(offset + 1)
        return True, indices
    result, indices = p(list, offset + 1, n, sum)
    if result:
            return result, indices
    return False, []


if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6, -7, -8, -9, -10, -11]
    print p(list, 0, 6, -10)
