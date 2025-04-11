# computational-geometry

## Closest-Pair problem
closest pair could be one from the left half, one from the right half, or the minimum of the two closest pairs from each half

### divide and conquer approach

1.Sort the points by their x-coordinates.

2.Divide the sorted list into two halves.

3.Recursively find the closest pair in each half.

4.Combine the results by checking for pairs that cross the two halves

by examining points within a **vertical strip** around the dividing line. This strip is checked efficiently by considering only points within a certain y-coordinate range.










### Prove that the intersection of two convex sets in the plane is convex
pick two arbitrary points

both belongs to A and B

line segment is a subset of A and B 

then line segment belongs to the intersection

### Prove that the smallest-perimeter polygon P containing a set P of points in the plane is convex.

by contradiction

Suppose there exists a non-convex polygon Q with the smallest possible perimeter that contains all points in P.

Since Q is non-convex, it has at least one reflex vertex B (where the internal angle is greater than 180 
∘). Let A, B, and C be three consecutive vertices of Q, with B as the reflex vertex.
 
triangle inequality,replace the two edges by a smaller edge than shape a convex.

**Let E be an unsorted set of n segments that are the edges of a convex polygon. Describe an
O(n log n)-time algorithm that computes from E a list containing all vertices of the polygon, sorted in clockwise
order**


find the leftmost and rightmost points O(n)+O(n)

above the line ,the upper 

sort the upper part by x ,sort the opposite by reverer order

**Let S be a set of n line segments in the plane. Prove that the convex hull of S is exactly the same as
the convex hull of the 2n endpoints of the segments**



**Consider the following alternative approach to computing the convex hull
of a set of points in the plane: We start with the rightmost point. This is
the first point p1 of the convex hull. Now imagine that we start with a
vertical line and rotate it clockwise until it hits another point p2. This is
the second point on the convex hull. We continue rotating the line but this
time around p2 until we hit a point p3. In this way we continue until we
reach p1 again.
a. Give pseudocode for this algorithm.
b. What degenerate cases can occur and how can we deal with them**

check all the points about the angle with vertical line O(n*h) h is the num of the points

reach the left most,then is the upper,change the direction 

**Design a divide-and-conquer algorithm for computing the convex hull of any given set of n points
in the plane. Do not forget to analyze the running time of your algorithm**


merge:


the highest  y for the interaction points with vertical line


**Let S be a set of n disjoint line segments whose upper endpoints lie on the
line y= 1 and whose lower endpoints lie on the line y= 0. These segments
partition the horizontal strip [−∞ : ∞] × [0 : 1] into n + 1 regions. Give an
O(n log n) time algorithm to build a binary search tree on the segmentsin S such that the region containing a query point can be determined in
O(log n) time. Also describe the query algorithm in detail.**



**The intersection detection problem for a set S of n line segments is to
determine whether there exists a pair of segments in S that intersect. Give
a plane sweep algorithm that solves the intersection detection problem in
O(n log n) time.**




**Let S be a set of n circles in the plane. Describe a plane sweep algorithm
to compute all intersection points between the circles. (Because we dealwith circles, not discs, two circles do not intersect if one lies entirely
inside the other.) Your algorithm should run in O((n + k) log n) time,
where k is the number of intersection points.**



**Let S be a set of n disjoint line segments in the plane, and let p be a
point not on any of the line segments of S. We wish to determine all
line segments of S that p can see, that is, all line segments of S that
contain some point q so that the open segment pq doesn’t intersect any
line segment of S. Give an O(n log n) time algorithm for this problem that
uses a rotating half-line with its endpoint at p**



**Let S be a set of n disjoint triangles in the plane, and let P be a set of m points in the plane.
Design an efficient algorithm to decide, for each point p of P , which triangles from S contains p, if any. What is the
running time of your algorithm?**






















