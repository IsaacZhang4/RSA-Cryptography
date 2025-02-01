import random
from typing import Tuple

# Type defs
Key = Tuple[int, int]

def isprime(n: int) -> bool:
    # Base cases
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Run Fermat's Primality Test
    for _ in range(100):
        a = random.randint(2, n - 2)
        if fast_mod_exp(a, n - 1, n) != 1:
            return False
    return True


def fast_mod_exp(a: int, expo: int, m: int) -> int:
    res = 1
    # Make usage of bit shift
    while expo > 1:
        if expo & 1:
            res = (res * a) % m
        a = a ** 2 % m
        expo >>= 1
    return (a * res) % m


def generate_prime(n: int) -> int:
    '''
    Description: Generate an n-bit prime number
    Args: n (No. of bits)
    Returns: prime number
    '''

    # Define maximum integer of n bits and minimum
    minimum = 2 ** (n - 1)
    maximum = 2 ** n

    while True:
        prime_candidate = random.randrange(minimum, maximum - 1)
        if prime_candidate % 2 != 0:  # Ensuring it's odd
            if isprime(prime_candidate):
                return prime_candidate


def generate_keypair(p: int, q: int) -> Tuple[Key, Key]:
    '''
    Description: Generates the public and private key pair
    if p and q are distinct primes. Otherwise, raise a value error

    Args: p, q (input integers)

    Returns: Keypair in the form of (Pub Key, Private Key)
    PubKey = (n,e) and Private Key = (n,d)
    '''
    if p == q or not isprime(p) or not isprime(q):
        raise ValueError
    n = p * q
    k = (p - 1) * (q - 1)
    e = generate_public_exponent(k)

    # In order to obtain d, we need to run the extended Euclid algorithm for the sake of inverse computation
    def extended_Euclid_GCD(a: int, b: int) -> tuple[int, int, int]:

        # Check if a is equal to 0 for base case, if so, return gcd, s, t as b, 0, 1
        if not a:
            return b, 0, 1

        # Recursive case where recursion condition will be (b mod a, a)
        else:
            gcd, t, s = extended_Euclid_GCD(b % a, a)
            return gcd, s - (b // a) * t, t

    # Function for computing the inverse with the result from the extended Euclid algorithm
    def inverse(a: int, m: int) -> int:

        # Get gcd, s, and t from the extended Euclid algorithm
        gcd, s, t = extended_Euclid_GCD(a, m)

        # Check if gcd is not 1, if it isn't, there is no inverse, otherwise return s mod m
        if gcd != 1:
            return None
        else:
            return s % m

    # Declare d as the inverse of e and k
    d = inverse(e, k)

    # Check if d is negative, if it is, multiply by -1
    if d < 0:
        d = d * (-1)

    if e == d or e == n or d == n:
        raise ValueError

    # Declare public and private keypairs as (n, e) and (n, d)
    public = (n, e)
    private = (n, d)

    # Return keypairs in format (public keypair, private keypair)
    return (public, private)


def gcd(a: int, b: int) -> int:
    # a = 0 means that b is our gcd
    if a == 0:
        return b
    # recursion condition will be (b mod a, a)
    return gcd(b % a, a)


def generate_public_exponent(k: int) -> int:
    '''
    Description: Helper function that generates the SMALLEST
    public exponent for a given k value.

    Args: k (integer)

    Returns: e (public exponent) (e > 2)
    '''
    # Define e starting at 3 and gcd as an integer variable
    e = 3
    greatest_common_denominator = int

    # Check if gcd is 1, if so, e is sufficient and should be outputted now
    if gcd(e, k) == 1:
        return e

    # Increase e by 1 until the gcd is 1, then output e
    while greatest_common_denominator != 1:
        e += 1
        greatest_common_denominator = gcd(e, k)
    return e