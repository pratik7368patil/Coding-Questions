# make function that compute GCD of given number using Euclid' Algorithm

def find_gcd(x, y):
    while y != 0:
        rem = x % y
        x = y
        y = rem
    return x  
print(find_gcd(124,400))