def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = round((low + high)/2) #calculate mid index
        guess = list[mid] #get mid value

        if guess == item:
            return mid #found the item
        
        if guess > item:
            high = mid - 1 #new high

        else:
            low = mid + 1 #new low
    
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1)) 


