from operator import itemgetter


def meeting(s):
    print(s)
    arr = s.split(";")
    arr = [item.split(":").reverse() for item in arr]
    my_str = ""
    for item in sorted(arr, key=lambda l: l[1]):
        my_str += "({0}, {1})".format(item[0].upper(), item[1].upper())
    print(my_str)
    return my_str
