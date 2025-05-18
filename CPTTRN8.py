'''CPTTRN8 - Character Patterns (Act 8)
#ad-hoc-1 #basics

Print a regular grid pattern with diamond-like base elements. Use the \ (backslash) and the / (slash) characters to print the borders and the * (asterisk) to print the inner part of the diamonds. Use . (dots) to fill the rest of the space.

Input
You are given t - the number of test cases and for each of the test cases three positive integers: r - the number of rows, c - the number of columns in the grid and s - the size of each diamond.

Output
For each of the test cases output the requested pattern (please have a look at the example). Use one line break in between successive patterns.
Problem Summary:
You are to print a grid of diamond shapes made of /, \, *, and . characters.

Each diamond is of size s:

Height and width of each diamond: 2 * s

Grid is of size r rows and c columns (number of diamonds)'''

def print_diamond_pattern(r, c, s):
    height = 2 * s
    width = 2 * s

    for row_block in range(r):
        for i in range(height):
            line = ""
            for col_block in range(c):
                for j in range(width):
                    if i + j == s - 1:
                        line += '/'
                    elif j - i == s:
                        line += '\\'
                    elif i - j == s:
                        line += '\\'
                    elif i + j == (3 * s - 1):
                        line += '/'
                    elif (s - 1 < i + j < 3 * s - 1) and (abs(i - j) < s):
                        line += '*'
                    else:
                        line += '.'
            print(line)
    print()

# Read input
t = int(input())
for _ in range(t):
    r, c, s = map(int, input().split())
    print_diamond_pattern(r, c, s)


