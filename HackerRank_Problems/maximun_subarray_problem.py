# we have to find maximum sum of subarray using Kadane's Algorithm

def find_max_subarray(arr):
    current_sum = 0
    best_sum = 0
    start = 0
    end = 0
    
    for current_end, x in enumerate(arr):
        if current_sum <= 0:
            current_start = current_end
            current_sum = x
        else:
            current_sum += x
        
        if current_sum > best_sum:
            best_sum = current_sum
            start = current_start
            end = current_end + 1
    print(arr[start: end])
    return best_sum


arr = [-11,22,33,-44]

print(find_max_subarray(arr))