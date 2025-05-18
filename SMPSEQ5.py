'''SMPSEQ5 - Fun with Sequences (Act 3)
#simple-math #basics

You are given a sequence of n integers S = s1, s2 ... sn and a sequence of m integers Q = q1, q2 ... qm.

Please print in ascending order all such i, that si = qi, i<=n, i<=m.

Input data specification
In the first line you are given one integer 2 <= n <= 100, and in the following line n integers:
-100 <= si <= 100, si <= si+1.

In the third line you are given one integer 2 <= m <= 100, and in the following line m integers:
-100 <= qi <= 100, qi <= qi+1.

Output data specification
The sequence of requested indexes separated by spaces.


ChatGPT said:
To solve SMPSEQ5 - Fun with Sequences (Act 3), you need to:

✅ Task:
Given two sorted sequences:

S = s1, s2, ..., sn

Q = q1, q2, ..., qm

Print all indices i (1-based) such that:

i ≤ n

i ≤ m

si == qi'''

# Read input
n = int(input())
S = list(map(int, input().split()))
m = int(input())
Q = list(map(int, input().split()))

# Determine the minimum length to compare
min_len = min(n, m)

# Find matching indices
matching_indices = [str(i+1) for i in range(min_len) if S[i] == Q[i]]

# Print the result
print(" ".join(matching_indices))
