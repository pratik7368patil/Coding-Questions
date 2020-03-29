# our task is to rearrange array [0,1,0,0,1,1,1] ---->> [0,0,0,1,1,1,1]

def rearrange(arr):
    arr_0 = []
    arr_1 = []
    for i in arr:
        if i == 0:
            arr_0.append(i)
        elif i == 1:
            arr_1.append(i)
    res = arr_0 + arr_1
    arr_0.clear()
    arr_1.clear()
    return res
    
arr = [0,1,0,0,1,1,1]
print(rearrange(arr))