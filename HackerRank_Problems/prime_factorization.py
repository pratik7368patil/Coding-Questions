## print and prime factors of given number in x**i, y**j,......
def prime_fact(n):
    if n == 0 or n == 1:
        print(None)
    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            count = 0
            while n % i == 0:
                n = n / i
                count += 1
            print("{}**{}".format(i, count), end = " ")
    if(n != 1): print("{}**{}".format(int(n),1))
                

n = 600851475143
prime_fact(n)