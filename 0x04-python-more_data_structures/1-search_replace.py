#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list1 = []
    for i in my_list:
        if i == search:
            list1.append(replace)
        else:
            list1.append(i)
    return (list1)
