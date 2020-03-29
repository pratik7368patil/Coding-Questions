def find_all_factors(n):
    i = 1
    res = list()
    while i <= n**0.5: 
        if (n % i == 0) : 
            if (n / i == i) : 
                res.append(i)
            else : 
                res.append(i)
                res.append(int(n/i))
        i = i + 1
    res.sort()
    return res
    
n = 96
print(find_all_factors(n))
