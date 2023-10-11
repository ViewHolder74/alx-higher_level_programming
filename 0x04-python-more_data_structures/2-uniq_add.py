#!/usr/bin/python3
def uniq_add(my_list=[]):
    num = set()
    uniq_sum = 0
    for i in my_list:
        if i not in num:
            num.add(i)
            uniq_sum += i
    return (uniq_sum)
