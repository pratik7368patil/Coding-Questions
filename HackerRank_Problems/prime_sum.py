# out task is to perform prime sum

def prime_sum(k):
    prime = []
    dummy = [True] * (k + 1)
    for p in range(2, k+1):
        if dummy[p]:
            prime.append(p)
        for i in range(p, k + 1, p):
            dummy[i] = False
    print(prime)
    for j in range(len(prime)):
        for x in range(j+1, len(prime)):
            if prime[j] + prime[x] == k:
                print("{} can be represented as sum of : ".format(k),prime[j], prime[x])
                
prime_sum(20)