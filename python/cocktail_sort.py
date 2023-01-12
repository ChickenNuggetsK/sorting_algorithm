def cocktail_sort(arr:list):
    sorted = False
    start = -1
    end = len(arr) - 1

    while sorted == False:
        sorted = True

        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
        
        end -= 1

        for i in range(end, start, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
        
        start += 1
    
    return arr
