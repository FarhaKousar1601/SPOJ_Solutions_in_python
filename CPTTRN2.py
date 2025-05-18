'''CPTTRN2 - Character Patterns (Act 2)
#basics

Using two characters: . (dot) and * (asterisk) print a frame-like pattern.

Input
You are given t - the number of test cases and for each of the test cases two positive integers: l - the number of lines and c - the number of columns of a frame.

Output
For each of the test cases output the requested pattern (please have a look at the example). Use one line break in between successive patterns.'''

t = int(input())
for _ in range(t):
    l, c = map(int, input().split())
    for i in range(l):
        line = []
        for j in range(c):
            # Border positions: first or last row, or first or last column
            if i == 0 or i == l-1 or j == 0 or j == c-1:
                line.append('*')
            else:
                line.append('.')
        print(''.join(line))
    print()  # blank line after each test case
