# our task is to find largest palindrome product of 3-digits of given number

def l_palin_pro(low, top):
    product = 0
    for i in range(low, top):
        for j in range(low, top):
            mul = str(i * j)
            if mul[::] == mul[::-1]:
                product = int(mul)
    return product
                
                
                
print(l_palin_pro(100, 999))