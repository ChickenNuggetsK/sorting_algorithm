def bubble_sort(arr:list)->list:
    for i in range(len(arr)-1, 0, -1):
        sorted = True
        
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                sorted = False
        
        if sorted:
            return arr
    return arr
