# our task is to find max absolute difference in array

def max_abs_diff(arr):
    res = 0
    stack = []
    
    for i in range(len(arr)):
        for j in range(i ,len(arr)):
            s = abs(arr[i] - arr[j]) + abs(i - j)
            stack.append(s)
    return max(stack)


arr = [ -70, -64, -6, -56, 64, 61, -57, 16, 48, -98 ] 
print(max_abs_diff(arr))