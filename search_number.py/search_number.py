def search_numnber_list(num:int, number_list:list[int]) -> bool:
    for i in range(len(number_list)):
        print (i)
        if number_list[i] == num:
            return True
    return False    
        
        
print(search_numnber_list(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))        



def search(num:int, numbers_list:list[int]):
    if num in numbers_list:
        return "It is present"
    return "It is not present"
        
print(search(2,[2,3,4,5,6,7]))
        