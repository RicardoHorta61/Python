def find_duplicate(list):
    duplicated_numbers = []
    list.sort()
    for i in range(1, len(list)):
        if list[i] == list[i-1]:
            duplicated_numbers.append(list[i])
    return duplicated_numbers
        
print(find_duplicate([3,2,2,1,3,5,6,8])) #2,3
print(find_duplicate([3,5,8,1,3,5,6,8])) #3,5,8