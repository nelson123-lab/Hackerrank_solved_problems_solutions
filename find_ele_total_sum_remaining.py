def find_even_index(arr):
    #your code here
    index = 0
    while index < len(arr):
        a = arr.pop(index)
        if sum(arr) == a:
            return index
        arr.insert(index, a)
        index +=1
    return -1
            
