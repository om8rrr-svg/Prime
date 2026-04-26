def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(limit):
    """Return a list of primes up to limit."""
    return [n for n in range(2, limit + 1) if is_prime(n)]

if __name__ == "__main__":
    number = 17
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

    print(f"Primes up to 50: {get_primes(50)}")
