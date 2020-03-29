## generate all prime numbers upto N using Sieve if Eratosthenes

def allPrime(n):
    if n == 1 or n == 0:
        print(None)
    sieve = [True] * (n+1)   ## generate list upto N+1 and consider all as prime
    for p in range(2, n + 1):
        if (sieve[p]):
            print(p)
        for i in range(p, n+1, p): ## 2 and multiple of two 
            sieve[i] = False

n = 15  
allPrime(n)

## if the number is prime then its multiples are not prime..... so remove them or set flase at their position