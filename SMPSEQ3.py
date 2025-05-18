'''SMPSEQ3 - Fun with Sequences
#basics

You are given a sorted sequence of n integers S = s1, s2 ... sn and a sorted sequence of m integers Q = q1, q2 ... qm.

Please print in ascending order all such si that does not belong to Q.

Input data specification
In the first line you are given one integer 2 <= n <= 100, and in the following line n integers:
-100 <= si <= 100, si <= si+1.

In the third line you are given one integer 2 <= m <= 100, and in the following line m integers:
-100 <= qi <= 100, qi <= qi+1.

Output data specification
The sequence of requested integers separated by spaces.


ChatGPT said:
To solve the SMPSEQ3 - Fun with Sequences problem, we need to:

Take two sorted input sequences:

S of length n

Q of length m

Print all integers from S that are not in Q, maintaining ascending order.'''

# Read inputs
n = int(input())
S = list(map(int, input().split()))
m = int(input())
Q = list(map(int, input().split()))

# Convert Q to a set for faster lookup
Q_set = set(Q)

# Filter and print elements from S not in Q
result = [str(s) for s in S if s not in Q_set]
print(" ".join(result))
