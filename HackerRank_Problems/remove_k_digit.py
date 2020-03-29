#Input:
#num = ‘1432219’
#k = 3
#Expected Output:
#‘1219’

#Input:
#num = ‘10’
#k = 2
#Expected Output:
#‘0’

def remove_k_digits(number, k):
    stack = []
    i=0
    while i<len(number):
           
        while stack and k and number[i]<stack[-1]:
            k-=1
            stack.pop()
        stack.append(number[i])
        i+=1
    if not k:
        ans=''.join(stack)
    else:
        ans=''.join(stack[:-k])+number[i:]
    return ans.lstrip('0') or '0'
                    


number = "98004650962809"   # output must be '1219'
k = 13
print(remove_k_digits(number, k))