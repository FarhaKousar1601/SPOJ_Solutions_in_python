'''SMPDIV - Divisibility
#simple-math #ad-hoc-1 #basics

Print all integers ai such that ai is divisible by x and not divisible by y, where 1 < ai < n < 100000.

Input
First, you are given t (t < 100) - the number of test cases. In each of the following t lines, 3 integers: n x y.

You might assume also that x < n and x is not divisible by y.'
Problem Restatement
For each test case, given integers n, x, and y, you need to print all integers a_i such that:

1 < a_i < n

a_i is divisible by x

a_i is not divisible by y

Input
t — number of test cases (less than 100)

For each test case, integers n, x, y

Output
For each test case, print all numbers a_i that satisfy the conditions on one line, separated by spaces.

Constraints and Notes
1 < a_i < n < 100000

x < n

x is not divisible by y

Approach
Iterate over multiples of x starting from x up to n-1.

For each multiple, check if it is NOT divisible by y.

If it meets the criteria, print it.
Explanation
Loop through multiples of x with range(x, n, x).

Check divisibility by y.

Collect valid numbers in a list and print them space-separated.'''


t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    result = []
    for num in range(x, n, x):
        if num % y != 0:
            result.append(str(num))
    print(" ".join(result))

