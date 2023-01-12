def selection_sort(arr:list)->list:
    for i in range(len(arr)-1):

        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
            
            if min != i:
                arr[min], arr[i] = arr[i], arr[min]
    
    return arr
