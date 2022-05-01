import math

#Can you come up with the base case and recursive case for binary search?
def search(arr, element, start, end): #start/ end to store index
    if start > end: 
        return None #element is not in the array

    mid = (start + end) // 2 #truncating division

    if arr[mid] == element: #base case
        return mid
    elif arr[mid] > element: #too high!
        return search(arr, element, start, mid-1) #eliminate indexes after mid-1
    else: #arr[mid] < element too low!
        return search(arr, element, mid+1, end) #eliminate indexes before mid+1
    
arr = [1,2,3,15,56,100]
print('Element in index: ' + str(search(arr, 444, 0, len(arr)-1)))