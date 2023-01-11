def odd_even_sort(arr:list)->list:
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr)-1, 2):

            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        
        for j in range(0, len(arr)-1, 2):

            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    
    return arr
