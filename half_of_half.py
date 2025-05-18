'''Given a sequence of 2*k characters, please print every second character from the first half of the sequence. Start printing with the first character.

Input
In the first line of input you are given the positive integer t (1<=t<=100) - the number of test cases. In the each of the next t lines, you are given a sequence of 2*k (1<=k<=100) characters.

Output
For each of the test cases please please print every second character from the first half of a given sequence (the first character should appear).'''

t = int(input())
for _ in range(t):
    s = input()
    half = len(s) // 2
    # print every second character from the first half, starting with the first character (index 0)
    result = s[:half:2]
    print(result)

'''Explanation:
For each test case, we read the string s.

The first half is s[:half].

We take every second character from that half starting at index 0 using s[:half:2].

Then print the result.'''
