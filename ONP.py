'''ONP - Transform the Expression
Transform the algebraic expression with brackets into RPN form (Reverse Polish Notation). Two-argument operators: +, -, *, /, ^ (priority from the lowest to the highest), brackets ( ). Operands: only letters: a, b ... z. Assume that there is only one RPN form (no expressions like a*b*c).

Input
t [the number of expressions <= 100]
expression [length <= 400]
[other expressions]
Text grouped in [ ] does not appear in the input file.

Output
The expressions in RPN form, one per line.

Example
Input:
3
(a+(b*c))
((a+b)*(z+x))
((a+t)*((b+(a+c))^(c+d)))

Output:
abc*+
ab+zx+*
at+bac++cd+^*


ChatGPT said:
To solve the ONP - Transform the Expression problem, you need to convert an infix expression (e.g. (a+(b*c))) into postfix expression (also known as Reverse Polish Notation, or RPN).

This is a classic problem solved using a stack, often with the Shunting Yard algorithm.

✅ Operator Precedence and Associativity
Operator	Precedence	Associativity
+ -	1	Left
* /	2	Left
^	3	Right

✅ Algorithm (Simplified for This Problem):
Operands (a–z): Add directly to the output.

Left Parenthesis (: Push to stack.

Right Parenthesis ): Pop from stack to output until ( is found (discard ().

Operators:

While top of stack is an operator and has higher precedence (or same precedence if left-associative), pop it to output.

Then push current operator.'''

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def is_right_associative(op):
    return op == '^'

def infix_to_postfix(expression):
    stack = []
    output = []
    for ch in expression:
        if ch.isalpha():
            output.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # remove '('
        else:  # operator
            while (stack and stack[-1] != '(' and
                   (precedence(stack[-1]) > precedence(ch) or
                   (precedence(stack[-1]) == precedence(ch) and not is_right_associative(ch)))):
                output.append(stack.pop())
            stack.append(ch)
    
    while stack:
        output.append(stack.pop())

    return ''.join(output)

# Read input
t = int(input())
for _ in range(t):
    expr = input().strip()
    print(infix_to_postfix(expr))



