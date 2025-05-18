'''SMPCIRC - Two Circles
#plane-geometry #basics

Given two circles: O1 with the center o1 = (x1, y1) and a radius r1 and O2 with the center o2 = (x2, y2) and radius r2, please compute if O1 is inside O2 or if O2 is inside O1.

Input

First t < 1000, the number of test cases. In each of the following t lines, 6 integers: x1 y1 r1 x2 y2 r2. Where 0 ≤ x1, y1, x2, y2 ≤ 10000 and 0 < r1, r2 ≤ 10000.

Output

For each test case print one character:

I, if O1 is inside O2 (or if O2 is inside O1),
E, if O1 is internally tangent to O2 (or if O2 is internally tangent to O1),
O, in other cases.


ChatGPT said:
To solve the SMPCIRC - Two Circles problem, we need to analyze the spatial relationship between two circles based on their centers and radii.

🔍 Problem Understanding
You're given:

t test cases

For each test case: x1 y1 r1 x2 y2 r2
(Center and radius of circle O1 and O2)

You need to determine:

I — if one circle is completely inside the other.

E — if one circle is internally tangent to the other.

O — otherwise (overlap, disjoint, or intersecting).

✅ Conditions
Let d be the distance between the centers of the two circles:d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
Let r_big = max(r1, r2) and r_small = min(r1, r2)

Now check:

Internally Tangent (E):
If d == abs(r1 - r2)

One Inside Another (I):
If d < abs(r1 - r2)

Other Cases (O):
Otherwise'''

import math

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.hypot(x2 - x1, y2 - y1)  # More accurate than sqrt(a^2 + b^2)
    
    radius_diff = abs(r1 - r2)

    if math.isclose(d, radius_diff, abs_tol=1e-6):  # Internally tangent
        print("E")
    elif d < radius_diff:  # One is inside the other
        print("I")
    else:  # Other cases
        print("O")


