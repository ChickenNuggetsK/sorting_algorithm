def comb_sort(arr:list)->list:
    gap = len(arr)
    sorted = False

    while gap > 1 or sorted == False:
        sorted = True
        gap = int(gap / 1.3)

        if gap < 1:
            gap = 1

        for i in range(len(arr) - gap):
            if arr[i] > arr[i+gap]:
                arr[i], arr[i+gap] = arr[i+gap], arr[i]
                sorted = False
    
    return arr
