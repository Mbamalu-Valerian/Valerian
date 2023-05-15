def sieve_of_eratosthenes(n):
    # Create a boolean array "is_prime[0..n]" and initialize all entries as True
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            # Mark all multiples of p as non-prime
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    # Return a list of prime numbers
    primes = [i for i in range(n + 1) if is_prime[i]]
    return primes


def print_prime_numbers(n):
    print("Prime numbers from 0 to", n, ":")
    primes = sieve_of_eratosthenes(n)
    for prime in primes:
        print(prime)


# Example usage
n = int(input("Enter a number: "))
print_prime_numbers(n)
