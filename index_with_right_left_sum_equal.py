def find_even_index(arr):
    #your code here
    index = 0
    while index < len(arr):
        if sum(arr[:index]) == sum(arr[index+1:]):
            return index
        index +=1
    return -1
            
