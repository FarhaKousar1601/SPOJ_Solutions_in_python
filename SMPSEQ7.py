'''SMPSEQ7 - Fun with Sequences (Act 5)
#simple-math #basics

You are given S - a sequence of n integers S = s1, s2 ... sn. Please, compute if it is possible to split S into two parts: s1, s2 ... si and si+1, si+2 ... sn (1 <= i < n) in such a way that the first part is strictly decreasing while the second is strictly increasing one.

Input data specification
In the first line you are given an integer 2 <= n <= 100 and in the following line n integers
-100 <= si <= 100.

Output data specification
One word Yes or No.


ChatGPT said:





You said:
SMPSEQ7 - Fun with Sequences (Act 5)
#simple-math #basics

You are given S - a sequence of n integers S = s1, s2 ... sn. Please, compute if it is possible to split S into two parts: s1, s2 ... si and si+1, si+2 ... sn (1 <= i < n) in such a way that the first part is strictly decreasing while the second is strictly increasing one.

Input data specification
In the first line you are given an integer 2 <= n <= 100 and in the following line n integers
-100 <= si <= 100.

Output data specification
One word Yes or No.


ChatGPT said:
To solve the SMPSEQ7 problem, we need to determine if a sequence can be split into two parts such that:

The first part is strictly decreasing.

The second part is strictly increasing.

There must be at least one element in both parts.

✅ Approach:
Loop over all possible split points i from 1 to n-1.

Check if the first part S[0:i] is strictly decreasing.

Check if the second part S[i:] is strictly increasing.

If such a split is found, print "Yes" and stop.

If no valid split is found after checking all positions, print "No".'''

n = int(input())
S = list(map(int, input().split()))

def is_strictly_decreasing(arr):
    return all(arr[i] > arr[i+1] for i in range(len(arr) - 1))

def is_strictly_increasing(arr):
    return all(arr[i] < arr[i+1] for i in range(len(arr) - 1))

found = False
for i in range(1, n):
    if is_strictly_decreasing(S[:i]) and is_strictly_increasing(S[i:]):
        found = True
        break

print("Yes" if found else "No")
