#Input: arr[] = {3, 1, 3}
#Output: Missing = 2, Repeating = 3
#Explanation: In the array, 
#2 is missing and 3 occurs twice 

#Input: arr[] = {4, 3, 6, 2, 1, 1}
#Output: Missing = 5, Repeating = 1

def find(arr):
    temp = [False] * (len(arr))
    for i in range(len(arr)):
        if temp[arr[i] - 1] == False:
            temp[arr[i] - 1] = True
        elif temp[arr[i] - 1] == True:
            print("Repeating Element is : ", arr[i])
    for x in range(len(temp)):
        if temp[x] == False:
            print("Missing element is : ", x + 1)
            
arr = [4, 3, 6, 2, 1, 1]
find(arr)
