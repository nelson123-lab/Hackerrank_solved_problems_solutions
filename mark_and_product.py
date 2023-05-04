def floor_store_finder(stores_list, no_of_stores):
    index = 0
    floor_no = 1
    store_no = 0
    for i in stores_list:
        if i <= no_of_stores[index]:
            store_no = i
            return floor_no,store_no
        else:
            index += 1
            floor_no += 1
            store_no = i-no_of_stores[index-1]
            return floor_no, store_no



n, m = list(map(int, input().split()))
no_of_stores = list(map(int, input().split()))
stores_list = list(map(int, input().split()))

print(floor_store_finder(stores_list, no_of_stores))
