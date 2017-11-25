# coding=utf-8

def swap(list, i1, i2):
    temp = list[i1]
    list[i1] = list[i2]
    list[i2] = temp


def sort(list, offset, len):
    if len <= 1:
        return
    number = list[offset]
    l = offset
    r = offset + len - 1
    while r > l:
        while r > l and list[r] >= number:
            r -= 1
        if r == l:
            swap(list, l, offset)
            break
        while r > l and list[l] <= number:
            l += 1
        if r == l:
            swap(list, l, offset)
            break
        swap(list, l, r)
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
