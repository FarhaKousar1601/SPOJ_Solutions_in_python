'''DIVSUM - Divisor Summation
#number-theory

Given a natural number n (1 <= n <= 500000), please output the summation of all its proper divisors.

Definition: A proper divisor of a natural number is the divisor that is strictly less than the number.

e.g. number 20 has 5 proper divisors: 1, 2, 4, 5, 10, and the divisor summation is: 1 + 2 + 4 + 5 + 10 = 22.

Input
An integer stating the number of test cases (equal to about 200000), and that many lines follow, each containing one integer between 1 and 500000 inclusive.

Output
One integer each line: the divisor summation of the integer given respectively.


ChatGPT said:
Here's an efficient solution for the problem DIVSUM - Divisor Summation.

Given the constraints:

Up to 200,000 test cases

Each number n ≤ 500,000

We must optimize the solution by precomputing the sum of proper divisors for all numbers up to 500,000.'''

import sys
input = sys.stdin.read

# Precompute divisor sums up to 500000
MAX = 500001
divisor_sum = [0] * MAX

# Fill using modified sieve
for i in range(1, MAX):
    for j in range(2 * i, MAX, i):
        divisor_sum[j] += i

# Read all input at once for speed
data = input().split()
t = int(data[0])
nums = list(map(int, data[1:]))

# Output results
output = []
for n in nums:
    output.append(str(divisor_sum[n]))

# Print all results at once
print("\n".join(output))
