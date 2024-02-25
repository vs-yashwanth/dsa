
def get_prime_numbers( n):
    
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, n+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    primes = []
    for i in range(2, n+1):
        if sieve[i]:
            primes.append(i)
    return primes


print(get_prime_numbers(100000))