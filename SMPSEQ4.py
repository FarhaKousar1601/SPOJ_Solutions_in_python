'''SMPSEQ4 - Fun with Sequences (Act 2)
#basics

You are given a sorted sequence of n integers S = s1, s2 ... sn and a sorted sequence of m integers Q = q1, q2 ... qm.

Please print in ascending order all such si that belongs to Q.

Input data specification
In the first line you are given one integer 2 <= n <= 100, and in the following line n integers:
-100 <= si <= 100, si <= si+1.

In the third line you are given one integer 2 <= m <= 100, and in the following line m integers:
-100 <= qi <= 100, qi <= qi+1.

Output data specification
The sequence of requested integers separated by spaces


ChatGPT said:
To solve SMPSEQ4 - Fun with Sequences (Act 2), we need to:

✅ Task:
From two sorted sequences:

S of length n

Q of length m

Print all elements from S that are also in Q (intersection), in ascending order.'''

# Read input
n = int(input())
S = list(map(int, input().split()))
m = int(input())
Q = list(map(int, input().split()))

# Convert Q to set for fast lookup
Q_set = set(Q)

# Filter only those in both S and Q
result = [str(s) for s in S if s in Q_set]

# Print result
print(" ".join(result))

