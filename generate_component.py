import random

def generate():
    primes = [i for i in range(10000,100000) if isPrime(i)]
    p = random.choice(primes)
    q = random.choice(primes)
    n= p * q
    x = random.randrange(1, n)
    return n, x


def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True