'''Peter wants to generate some prime numbers for his cryptosystem. Help him! Your task is to generate all prime numbers between two given numbers!

Input
The input begins with the number t of test cases in a single line (t ≤ 10). In each of the next t lines there are two numbers m and n (1 ≤ m ≤ n ≤ 1000000000, n-m ≤ 100000) separated by a space.

Output
For every test case print all prime numbers p such that m ≤ p ≤ n, one number per line, test cases separated by an empty line.

Example
Input:
2
1 10
3 5

Output:
2
3
5
7

3
5'''

'''Solve the PRIME1 - Prime Generator problem efficiently (especially given the large constraints), you should use a technique called the Segmented Sieve of Eratosthenes.

✅ Problem Constraints Recap:
Up to 10 test cases.

1 ≤ m ≤ n ≤ 10^9, with n - m ≤ 100000.

You need to generate all prime numbers in the range [m, n] for each test case.

Efficient I/O is necessary due to large data.

✅ Why Segmented Sieve?
A simple sieve works up to n ≈ 10^6, but here n can be 10^9.

The segmented sieve first finds all primes up to √n using a normal sieve.

Then it marks non-primes in the range [m, n] using those base primes.'''

import sys
import math

def simple_sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i*i, limit+1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

def segmented_sieve(m, n):
    limit = int(math.sqrt(n)) + 1
    primes = simple_sieve(limit)
    
    is_prime = [True] * (n - m + 1)

    for p in primes:
        # Find the minimum number in [m, n] that is a multiple of p
        start = max(p * p, ((m + p - 1) // p) * p)
        for j in range(start, n + 1, p):
            is_prime[j - m] = False
    
    result = []
    for i in range(n - m + 1):
        if is_prime[i] and (m + i) > 1:
            result.append(str(m + i))
    return result

# Read all input at once (for speed)
input = sys.stdin.read().split()
t = int(input[0])
index = 1

outputs = []

for _ in range(t):
    m = int(input[index])
    n = int(input[index + 1])
    index += 2
    primes_in_range = segmented_sieve(m, n)
    outputs.append('\n'.join(primes_in_range))

# Print with blank line between test cases
print('\n\n'.join(outputs))
