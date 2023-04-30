def find_duplicate(list):
    list.sort()
    for i in range(1, len(list)):
        if list[i] == list[i-1]:
            return list[i]
        
print(find_duplicate([3,2,1,3,5,6,8]))