import random
j = 0
sollist = []

def strand_sort(arr:list)->list:
    global j, sollist
    
    if len(arr) == 0:
        return sollist
    
    else:
        sublist = []
        sublist.append(arr[0])
        arr.pop(0)

        index = 0
        i = 0
        while i < len(arr):
            if arr[i] > sublist[index]:
                sublist.append(arr[i])
                arr.pop(i)
                i -= 1
                index += 1
            i += 1
        
        if j == 0:
            for i in range(len(sublist)):
                sollist.append(sublist[i])
                j += 1
        
        else:
            subend = len(sublist) - 1
            solstart = 0

            while len(sublist) != 0:
                if sublist[subend] > sollist[solstart]:
                    solstart += 1
                
                else:
                    sollist.insert(solstart, sublist[subend])
                    sublist.pop(subend)
                    subend -= 1
                    solstart = 0
        

        return strand_sort(arr)


arr = [random.randint(0, 999999) for i in range(1000)]
print(strand_sort(arr))