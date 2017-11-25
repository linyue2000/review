# coding=utf-8

def sort(list, offset, len):
    if len <= 1:
        return
    number = list[offset]
    l = offset
    r = offset + len - 1
    while r > l:
        for r in xrange(r, l - 1, -1):
            if list[r] < number:
                break
        else:
            list[l], list[offset] = list[offset], list[l]
            break
        for l in xrange(l, r + 1):
            if list[l] > number:
                break
        else:
            list[l], list[offset] = list[offset], list[l]
            break
        list[l], list[r] = list[r], list[l]
    sort(list, offset, l - offset)
    sort(list, l + 1, offset + len - (l + 1))


if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6]
    sort(list, 0, len(list))
    print list

    list = [6, 5, 4, 3, 2, 1]
    sort(list, 0, len(list))
    print list

    list = [3, 6, 4, 1, 2, 5]
    sort(list, 0, len(list))
    print list

    list = [6, 6, 6, 6, 6, 6]
    sort(list, 0, len(list))
    print list

    list = [1, 9, 6, 6, 6, 6]
    sort(list, 0, len(list))

    print list
