# coding=utf-8

# 算法导论 思考题2.4

def merge(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    i = 0
    j = 0
    sum = 0
    list = []
    while i < len1 or j < len2:
        if i == len1:
            list.append(list2[j])
            j += 1
        elif j == len2:
            list.append(list1[i])
            i += 1
        else:
            if list1[i] < list2[j]:
                list.append(list1[i])
                i += 1
            else:
                sum += (len1 - i)
                list.append(list2[j])
                j += 1
    return list, sum


def sort(list):
    list_len = len(list)
    if list_len == 1:
        return list, 0
    else:
        list1, sum1 = sort(list[0:list_len / 2])
        list2, sum2 = sort(list[list_len / 2: list_len])
        list, sum3 = merge(list1, list2)
        return list, sum1 + sum2 + sum3


if __name__ == '__main__':
    list = [2, 3, 8, 6, 1]
    list_len = len(list)
    print sort(list)
    list = [6, 5, 4, 3, 2, 1]
    list_len = len(list)
    print sort(list)
    list = [1, 2, 3, 4, 5, 6]
    list_len = len(list)
    print sort(list)
