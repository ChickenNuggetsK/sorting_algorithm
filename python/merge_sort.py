def merge(arr1:list, arr2:list)->list:
    if len(arr1) == 0:
        return arr2
    
    if len(arr2) == 0:
        return arr1
    
    if arr1[0] <= arr2[0]:
        return [arr1[0]] + merge(arr1[1:], arr2)
    
    else:
        return [arr2[0]] + merge(arr1, arr2[1:])

def merge_sort(arr:list)->list:
    if len(arr) <= 1:
        return arr
    
    else:
        return merge(merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:]))
