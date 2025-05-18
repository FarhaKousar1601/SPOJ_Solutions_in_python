'''HS12MBR - Minimum Bounding Rectangle
#plane-geometry #basics

Compute the Minimum Bounding Rectangle (MBR) that surrounds the given set of 2D objects, i.e., the axis-aligned rectangle, which contains all of the specified objects and is the one with minimum area among all rectangles with this property.

Input
First, you are given t (t<100) - the number of test cases.

Each of the test cases starts with one integer n (n < 100) - the number of objects in the set. In the successive n lines, the descriptions of the objects follow.

Each object is described by one character and some parameters:

a point: p x y, where x and y are point coordinates.
a circle: c x y r, where x and y are the center coordinates and r is the radius of the circle.
a line segment: l x1 y1 x2 y2, where xi, yi are the coordinates of the endpoints of the line.
Successive test cases are separated by an empty line.

Output
For each of the test cases output four numbers - the coordinates of the two points that correspond to the lower left and the upper right corner of the MBR, in the following order: first the x-coordinate of the lower left corner, then the y-coordinate of the lower left corner, the x-coordinate of the upper right corner and the y-coordinate of upper right corner.

You can assume that all object parameters are integers and that -1000 -1000 1000 1000 is a bounding rectangle for all of them.
Problem Restatement:
Given multiple 2D geometric objects (points, circles, line segments), find the smallest axis-aligned bounding rectangle that encloses all objects.

Input:
t test cases

For each test case:

n number of objects

Then n lines, each describing an object:

Point: p x y

Circle: c x y r

Line segment: l x1 y1 x2 y2

Test cases separated by a blank line.

Output:
For each test case, print the bounding rectangle defined by two points:

lower-left corner (xmin, ymin)

upper-right corner (xmax, ymax)

Approach:
Initialize xmin, ymin, xmax, ymax with large/small values or bounding limits (-1000, 1000 as given)

For each object:

Point: update bounding box with (x,y)

Circle: update bounding box with (x-r, y-r) and (x+r, y+r)

Line segment: update bounding box with both endpoints (x1,y1) and (x2,y2)

After processing all objects, print the bounding rectangle coordinates.'''

t = int(input())
for _ in range(t):
    n = int(input())
    
    xmin, ymin = 1001, 1001
    xmax, ymax = -1001, -1001
    
    for _ in range(n):
        parts = input().split()
        obj_type = parts[0]
        
        if obj_type == 'p':
            x, y = int(parts[1]), int(parts[2])
            xmin = min(xmin, x)
            ymin = min(ymin, y)
            xmax = max(xmax, x)
            ymax = max(ymax, y)
            
        elif obj_type == 'c':
            x, y, r = int(parts[1]), int(parts[2]), int(parts[3])
            xmin = min(xmin, x - r)
            ymin = min(ymin, y - r)
            xmax = max(xmax, x + r)
            ymax = max(ymax, y + r)
            
        elif obj_type == 'l':
            x1, y1, x2, y2 = map(int, parts[1:5])
            xmin = min(xmin, x1, x2)
            ymin = min(ymin, y1, y2)
            xmax = max(xmax, x1, x2)
            ymax = max(ymax, y1, y2)
    
    # Read the blank line after each test case (except last)
    if _ < t-1:
        input()
    
    print(xmin, ymin, xmax, ymax)
