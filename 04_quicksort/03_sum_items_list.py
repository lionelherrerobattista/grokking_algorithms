#Write a recursive function to count the number of items in a list.

from itertools import count


def sum(list):
    if len(list) == 0: #base case
        return 0
    else: #recursive case
        list.pop(0)
        totalElements = 1 + sum(list)
        return totalElements

def sum2(list):
    if list == []:
        return 0
    return 1 + sum2(list[1:])

print(sum([1,2,3,4,5]))