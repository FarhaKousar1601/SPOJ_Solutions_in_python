'''Your program is to use the brute-force approach in order to find the Answer to Life, the Universe, and Everything. More precisely... rewrite small numbers from input to output. Stop processing input after reading in the number 42. All numbers at input are integers of one or two digits.

Interactive Protocol
You should communicate with Judge using standard input and output.

Attention: the program should clear the output buffer after printing each line.

It can be done using fflush(stdout) command or by setting the proper type of buffering at the beginning of the execution - setlinebuf(stdout).
Each time the judge will give you a number. You should rewrite this number to standard output. If this number equals 42, after rewriting your program should terminate immediately.

Example
The example of communication.

Input:
3
15
42

Output:
3
15
42
Attention: the program should clear the output buffer after printing each line.'''

'''Problem Summary (Simplified):
You will receive numbers as input.

You must print each number immediately.

Stop reading/printing when the number 42 appears (but you still print 42).

After every output, flush the output buffer so the judge sees your answer immediately.'''

import sys

while True:
    try:
        n = int(input())        # Read input from the judge
        print(n, flush=True)    # Print and immediately flush the output
        if n == 42:
            break               # Stop if the number is 42
    except EOFError:
        break                   # In case input ends unexpectedly
