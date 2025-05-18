'''SBSTR1 - Substring Check (Bug Funny)
Given two binary strings, A (of length 10) and B (of length 5), output 1 if B is a substring of A and 0 otherwise.

Please note, that the solution may only be submitted in the following languages: Brainf**k, Whitespace and Intercal.

Input
24 lines consisting of pairs of binary strings A and B separated by a single space.

Output
The logical value of: 'B is a substring of A'.

Example
First two lines of input:

1010110010 10110
1110111011 10011

First two lines of output:
1
0
This problem is very simple in terms of logic — you just need to check whether the 5-character binary string B is a substring of the 10-character binary string A.

✅ Problem Summary:
Input: 24 lines, each with two binary strings:

A: 10 characters

B: 5 characters

Output: For each line, print 1 if B is a substring of A, else print 0.

You are supposed to submit in esoteric languages, but for understanding or practice, here’s how to solve it in Python:'''

for _ in range(24):
    A, B = input().split()
    print(1 if B in A else 0)


