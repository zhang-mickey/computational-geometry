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




**Describe algorithms to insert and detele points from a kd-tree.In your algorithm you do not need to take care of rebalancing the structure**

For insertion,start at the root and compare the point's coordinate in the current splitting dimension. If it's less than the node's value, go left; otherwise, go right. 
Continue this recursively until  finding a null spot where you can add the new node.
just finding the correct path based on the splitting dimensions and adding the new node as a leaf or internal node where appropriate.

Deletion ,the node to delete is a leaf, it's simple—just remove it.



**Describe algorithms to insert and detele points from a range tree.In your algorithm you do not need to take care of rebalancing the structure**

insert in the main tree,do binary search at every nodes. for all the effected parents,walk back and do binary search on y coordinates.


**Theorem 5.8 showed that a range tree on a set of n points in the plane requires O(nlogn) storage. One could bring down the storage requirements by storing associated structures only with a subset of the nodes in the main tree.

a. Suppose that only the nodes with depth 0, 2, 4, 6, . . . have an associated
structure. Show how the query algorithm can be adapted to answer
queries correctly.

skip 

b. Analyze the storage requirements and query time of such a data structure.

nlogn/2

squar(logn)

c. Suppose that only the nodes with depth 0, 1/j
logn., 2/j
logn., . . . have
an associated structure, where "j "  is a constant. Analyze the storage
requirements and query time of this data structure. Express the bounds
in n and j.
**

storage:j times n

query:2^(1/j logn) squar(logn)

**One can use the data structures described in this chapter to determine
whether a particular point (a,b) is in a given set by performing a range
query with range [a : a]×[b : b].

a. Prove that performing such a range query on a kd-tree takes time
O(logn).

O(n)=O(1)+O(n/2)

b. What is the time bound for such a query on a range tree? Prove your
answer.**

O(logn)

**In some applications one is interested only in the number of points that
lie in a range rather than in reporting all of them. Such queries are often
referred to as range counting queries. In this case one would like to avoid
having an additive term of O(k) in the query time.

a. Describe how a 1-dimensional range tree can be adapted such that a
range counting query can be performed in O(logn) time. Prove the
query time bound.

each internal node stores the total number of nodes in its subtree ,if it is a leaf, size=1,if it have left and right children,size=left_children_size+right_children_size 

Traverse​ the tree to find the split node where paths to a and b diverge.
​Sum​ sizes of subtrees that fall entirely within [a, b] during traversal.
​Avoid​ traversing subtrees outside the range.
Range counting: O(logn) due to subtree size aggregation

b. Using the solution to the 1-dimensional problem, describe how d dimensional
range counting queries can be answered in O(log d n)
time. Prove the query time 
**
<img width="879" alt="image" src="https://github.com/user-attachments/assets/44e3c49c-078c-4451-9f5f-d3485924afa6" />


**Let S1 be a set of n disjoint horizontal line segments and let S2 be a set
of m disjoint vertical line segments. Give a plane-sweep algorithm that
counts in O((n+m) log(n+m)) time how many intersections there are
in S1 /S2.**




**Give an example of a set of n line segments with an order on them that
makes the algorithm create a search structure of size $(n2) and worst-case
query time $(n).**


**Show that, given a planar subdivision S with n vertices and edges and a query point q, the face of
S containing q can be computed in time O(n). Assume that S is given in a doubly-connected edge list.**

<img width="854" alt="image" src="https://github.com/user-attachments/assets/16f2a0f4-b378-44cb-ab12-318437f61b8e" />




**Given a convex polygon P as an array of its n vertices in sorted order along the boundary. Show
that, given a query point q, it can be tested in time O(log n) whether q lies inside P**


**Given a y-monotone polygon P as an array of its n vertices in sorted order along the boundary.
Can you generalize the solution to the previous exercise to y-monotone polygons?**


**Design a deterministic algorithm, that is, one that does not make random choices, to compute the
trapezoidal map of a set of non-crossing line segments. Use the plane sweep paradigm from Chapter 2. The worst-case
running time of the algorithm should be O(n log n)**

**(6.16)The ray shooting problem occurs in computer graphics (see Chapter 8).
A 2-dimensional version can be given as follows: Store a set S of n
non-crossing line segments such that one can quickly answer queries
of the type: “Given a query ray &—a ray is a half-line starting at some
point—find the first segment in S intersected by &.” (We leave it to you to
define the behavior for degenerate cases.)
In this exercise, we look at vertical ray shooting, where the query ray
must be a vertical ray pointing upwards. Only the starting point need be
specified in such a query.
Give a data structure for the vertical ray shooting problem for a set S of
n non-crossing line segments in general position. Bound the query time
and storage requirement of your data structure. What is the preprocessing
time?
Can you do the same when the segments are allowed to intersect each
other?**



**Prove that for any n > 3 there is a set of n point sites in the plane such that one of the cells of
Vor(P ) has n − 1 vertices.**


placing n−1 points equally spaced on a circle around a central point would result in the central Voronoi cell being a regular (n−1)-gon with n−1 vertices


**Prove that any algorithm for computing the Voronoi diagram of a set of n point sites in the plane
needs Ω(n log n) in the worst-case.**

use a reduction from the sorting problem，which is known to have a lower bound of Ω(nlogn) 

or by contra

suppose faster than Ω(n log n)




**Let P be a set of n points in the plane. Give an O(n log n) time algorithm to find two points in P
that are closest together**

By using a divide and conquer approach with careful merging and strip processing, we can find the closest pair of points in a set P of n points in the plane in O(nlogn) time.

keep the minmum



**Let P be a set of n points in the plane. Give an O(n log n) time algorithm to find for each point p
in P another point in P that is closest to it.**


**Let the Voronoi diagram of a point set P be stored in a doubly-connected
edge list inside a bounding box. Give an algorithm to compute all points
of P that lie on the boundary of the convex hull of P in time linear in the
output size. Assume that your algorithm receives as its input a pointer to
the record of some half-edge whose origin lies on the bounding box.**

Each convex hull point's Voronoi cell touches the bounding box exactly once

**Use Euler’s formula to show that the maximum number of faces is n2/2+n/2+1 in an arrangement
with n(n − 1)/2 vertices and n2 edges**

**Let L be a set of n lines in the plane. Give an O(n log n) time algorithm to compute an axis-parallel
rectangle that contains all the vertices of A(L) in its interior.**

sort the line by slope

<img width="809" alt="image" src="https://github.com/user-attachments/assets/239f3fd5-3362-4d22-8f34-0e88e7ffbb75" />

**Let R be a set of n red points in the plane, and let B be a set of n blue
points in the plane. We call a line ℓ a separator for R and B if ℓ has
all points of R to one side and all points of B to the other side. Give a
randomized algorithm that can decide in O(n) expected time whether R
and B have a separator.**
<img width="887" alt="image" src="https://github.com/user-attachments/assets/f2f46103-449b-432f-8baf-9c3ff10ca243" />

**Given a set L of n lines in the plane, give an O(n log n) time algorithm to compute the maximum
level of any vertex in the arrangement A(L)**

**Let S be a set of n points in the plane. Give an O(n2) time algorithm to find the line containing
the maximum number of points in S**


**A simple polygon P is called star-shaped if it contains a point q such that for any point p in P
the line segment pq is contained in P. Give an algorithm whose expected running time is linear to decide whether a
simple polygon is star-shaped or not.**
![image](https://github.com/user-attachments/assets/f37c3ce1-be79-4c00-96bf-d81a9495ba77)

The idea is to model the constraints imposed by the polygon's edges as a system of linear inequalities。
Without loss of generality, we assume that the simple polygon P is represented by a counter clockwise chain of its vertices (numbering n) in array form. Given such a chain, it is straightforward to compute the lines representing each edge. Further, these lines can be converted into half-spaces facing the inside of P using orientation primitives.There are n such inequalities (one per edge), forming a system of linear constraints.  **Using a randomized linear programming algorithm**, we achieve the required expected linear time complexity .


**On n parallel railway tracks n trains are going with constant speeds v1, v2, . . . , vn . At time t = 0,
the trains are at positions k1, k2, . . . , kn. Give an O(n log n)-time algorithm that detects all trains that at some moment
in time are leading. To this end, use the algorithm for computing the intersection of half-planes.**

We model the problem in the (t,x)-plane:
Each train's position function x=vit+ki defines a line in the plane.

We are interested in the upper envelope of these lines, i.e., the set of all points (t,x) such that x≥v 
it+ki for all i

Use an efficient algorithm to compute the intersection of these n half-planes in 2D. This results in a convex polygonal region (possibly unbounded). The boundary of this region is the upper envelope of the lines.

Traverse the boundary of the convex region. Each edge of the boundary corresponds to a line from the original set of trains. Collect all such lines.The trains whose lines appear on the boundary are the ones that are leading at some time.
