'''SMPSUM - Iterated sums
#basics

Please compute the sum of squares for the given numbers: a, a+1, ..., b-1, b.

Input
Two numbers: a and b separated by space, where 1 <= a <= b <=100.

Output
Computed sum: a*a + (a+1)*(a+1) + ... + (b-1)*(b-1) + b*b


ChatGPT said:
To solve SMPSUM - Iterated Sums, we need to compute the sum of squares from a to b (inclusive):'''

a, b = map(int, input().split())
total = sum(i * i for i in range(a, b + 1))
print(total)

