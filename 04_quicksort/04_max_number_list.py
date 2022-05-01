#Find the maximum number in a list.
def maxNumber(arr):
    if len(arr) == 0:
        errorMessage = 'Empty array!!'
        return errorMessage
    elif len(arr) == 1: #base case - should be comparison between two numbers ??
        max = arr[0]
        return max
    else: #recursive case
        auxNumber = arr.pop(len(arr)-2) #compare with previous index - backwards. Pop element -divide and conquer-
        max = maxNumber(arr) #store max for comparison
        if auxNumber < max:
            return max
        else:
            return auxNumber

def maxNumber2(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print(maxNumber([1,56,2,4]))
