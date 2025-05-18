'''CPTTRN1 - Character Patterns (Act 1)
#basics

Using two characters: . (dot) and * (asterisk) print a chessboard-like pattern. The first character printed should be * (asterisk).

Input
You are given t < 100 - the number of test cases and for each of the test cases two positive integers: l - the number of lines and c - the number of columns in the pattern (l, c < 100).

Output
For each of the test cases output the requested pattern (please have a look at the example). Use one line break in between successive patterns.'''

t = int(input())
for _ in range(t):
    l, c = map(int, input().split())
    for i in range(l):
        line = []
        for j in range(c):
            # If sum of row and column index is even, print '*', else '.'
            if (i + j) % 2 == 0:
                line.append('*')
            else:
                line.append('.')
        print(''.join(line))
    print()  # blank line after each test case

'''How it works:
For each test case, read number of lines l and columns c.

For each position (i, j), if (i + j) is even, print * else print ..

Print a blank line after each pattern as required.'''
