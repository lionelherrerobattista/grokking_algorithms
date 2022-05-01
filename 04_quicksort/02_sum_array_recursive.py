#sum array - divide an conquer recursion
def sum(arr):
    if len(arr) == 0: #base case
        return 0
    else:
        total = arr.pop(0) + sum(arr) #recursive case
        return total

def sum2(list):
    if list == []:
        return 0
    return list[0] + sum2(list[1:]) #: operator == slice()

print(sum([1,2,3,4]))
print(sum2([1,2,3,4]))
