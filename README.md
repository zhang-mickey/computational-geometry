# concept
A half-plane in the plane:y≤m·x+c or y≥m·x+c

Line segments are assumed to be closed =with endpoints,not open


**non-crossing**
![image](https://github.com/user-attachments/assets/fe2d893a-728e-42b0-8fef-6093470db8c8)


## Closest-Pair problem
closest pair could be one from the left half, one from the right half, or the minimum of the two closest pairs from each half
Describe a plane sweep algorithm to find the closes pair of a set of n points in 2D space in O(nlogn) time. 
![image](https://github.com/user-attachments/assets/cb5c1737-2576-4dbb-b31b-8d0034a8fc27)


### divide and conquer approach

1.Sort the points by their x-coordinates.

2.Divide the sorted list into two halves.

3.Recursively find the closest pair in each half.

4.Combine the results by checking for pairs that cross the two halves

by examining points within a **vertical strip** around the dividing line. This strip is checked efficiently by considering only points within a certain y-coordinate range.



# convex hull

## compute leftmost upmost... inO(nlogn)
![image](https://github.com/user-attachments/assets/452efdbd-e35d-4c04-abc4-3173abbc17b1)




### Describe an O(nlogn) time method for determining if two sets A and B of n points in the plane can be separated by a line.
First, note that A and B can be separated by a line if and only if their convex hulls do not overlap. So our method will rst compute the convex hulls of A and B. This takes O(nlogn) time.

So our method will rst compute the convex hulls of A and B. This takes O(nlogn) time.Then we compute all of the line segment intersections for the two convex hulls. If we nd a single intersection, we stop. This also takes O(nlogn) time. (See Chapter 2.) Therefore, our complete algorithm takes O(nlogn) time. 


### 1.1(a) Prove that the intersection of two convex sets in the plane is convex
pick two arbitrary points

both belongs to A and B

line segment is a subset of A and B 

then line segment belongs to the intersection

### 1.1(b) Prove that the smallest-perimeter polygon P containing a set P of points in the plane is convex.

by contradiction

Suppose there exists a non-convex polygon Q with the smallest possible perimeter that contains all points in P.

Since Q is non-convex, it has at least one reflex vertex B (where the internal angle is greater than 180 
∘). Let A, B, and C be three consecutive vertices of Q, with B as the reflex vertex.
 
triangle inequality,replace the two edges by a smaller edge than shape a convex.

![image](https://github.com/user-attachments/assets/bf03ce99-0029-414e-993b-b9f1595fe76b)


**1.3 Let E be an unsorted set of n segments that are the edges of a convex polygon. Describe an
O(n log n)-time algorithm that computes from E a list containing all vertices of the polygon, sorted in clockwise
order**


find the leftmost and rightmost points O(n)+O(n)

above the line ,the upper 

sort the upper part by x ,sort the opposite by reverer order
![image](https://github.com/user-attachments/assets/5487c40b-aef1-4479-8700-5032520d7d3d)
![image](https://github.com/user-attachments/assets/85b6c219-e883-45c4-beba-66c507d3c275)


### 1.6（a）Let S be a set of n line segments in the plane. Prove that the convex hull of S is exactly the same as the convex hull of the 2n endpoints of the segments
![image](https://github.com/user-attachments/assets/c5c538fa-c912-41bb-869b-2d772e9c7732)

**1.7Consider the following alternative approach to computing the convex hull
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


### 1.8 Design a divide-and-conquer algorithm for computing the convex hull of any given set of n points in the plane. Do not forget to analyze the running time of your algorithm

![image](https://github.com/user-attachments/assets/d5d8ec7e-126e-4903-aa6b-dc02acf5f632)
![image](https://github.com/user-attachments/assets/1a434c88-bdd6-4a9c-95d5-80e73ab94d54)
![image](https://github.com/user-attachments/assets/b6d33600-e8fc-4376-878e-ea22f596be5f)

merge:


the highest  y for the interaction points with vertical line

![image](https://github.com/user-attachments/assets/d56aa3de-90c0-477e-b5e1-a64655529263)




Given a set P of points in the plane, let CH(P) denote the convex hull of P. 
**(a) Assume that the points in P are sorted from left to right. Give an O(n) algorithm to compute CH(P), where you can use any algorithm described in the book without having to describe it in detail. Motivate the time complexity.**

If the points in P are sorted from left to right by x-coordinate, we can compute the convex hull in O(n) time
Each point is pushed and popped at most once per hull (lower and upper), so the total work is O(n).Since the input is already sorted, we avoid the O(n log n) sorting step.

**(b) Considering the algorithm you suggested for the above question, what errors may occur, if any, in the presence of rounding errors in the floating point arithmetic? (2p)**
The convex hull algorithm depends on determining the orientation (left turn, right turn, or colinear) of triplets of points using the cross product:
If three points are nearly colinear, rounding may cause an incorrect orientation.
	•	This can lead to:
	•	Excluding points that should be on the hull.
	•	Including extra points that shouldn’t be on the hull.
	•	Incorrect turning decisions (e.g., interpreting a left turn as colinear or right turn).
 
![image](https://github.com/user-attachments/assets/85bc8f3e-b312-43a9-bf09-ed90708f601f)


# Line segment interaction
![image](https://github.com/user-attachments/assets/326f0ff8-2dd2-4acb-8eab-41f31d8fda0d)


![image](https://github.com/user-attachments/assets/10fa7ae2-fffc-463b-b6d2-fe2ac0cc238c)

## Doubly connected edge list（DCEL）: common edge-based representation

![image](https://github.com/user-attachments/assets/d129430d-35ac-49e8-9494-279aa6c7984a)


#### Twin(Prev(Twin(e))) ≠ Next(e) 



**（2.1）Let S be a set of n disjoint line segments whose upper endpoints lie on the
line y= 1 and whose lower endpoints lie on the line y= 0. These segments
partition the horizontal strip [−∞ : ∞] × [0 : 1] into n + 1 regions. Give an
O(n log n) time algorithm to build a binary search tree on the segmentsin S such that the region containing a query point can be determined in
O(log n) time. Also describe the query algorithm in detail.**


![image](https://github.com/user-attachments/assets/d30c0a22-0bb3-4980-ac0e-c5adc4525e15)

**（2.2）The intersection detection problem for a set S of n line segments is to
determine whether there exists a pair of segments in S that intersect. Give
a plane sweep algorithm that solves the intersection detection problem in
O(n log n) time.**

determine whether any two intersect (not find all intersections).

We run the plane sweep algorithm given in the text for line segment intersection, but we stop if we discover an intersection. 
This takes O(nlogn) time, because in the worst case we will have to process the events for the endpoints of each edge, each of which takes O(logn) time.
![image](https://github.com/user-attachments/assets/eee1b5b4-0c1b-4189-bb97-773f592c25df)



**（2.11）Let S be a set of n circles in the plane. Describe a plane sweep algorithm
to compute all intersection points between the circles. (Because we dealwith circles, not discs, two circles do not intersect if one lies entirely
inside the other.) Your algorithm should run in O((n + k) log n) time,
where k is the number of intersection points.**
![image](https://github.com/user-attachments/assets/34f3f218-3e29-402b-a0d0-b82db70e23f9)
![image](https://github.com/user-attachments/assets/607b47d7-533c-40b3-9eeb-f7eb4cd99ab1)
![image](https://github.com/user-attachments/assets/1142a111-625a-4726-afa9-f074fddd885e)

We can break each circle into 2 semicircles with a vertical line crossing their centers. Instead of line segments, we can perform the sweep line algorithm on the 2n semicircles. The only difference is that we have to distinguish the “intersection” of two semicircles from a common circle, and that the itersection between circles can be twice.

**（2.14）Let S be a set of n disjoint line segments in the plane, and let p be a
point not on any of the line segments of S. We wish to determine all
line segments of S that p can see, that is, all line segments of S that
contain some point q so that the open segment pq doesn’t intersect any
line segment of S. Give an O(n log n) time algorithm for this problem that
uses a rotating half-line with its endpoint at p**

This is still similar to plane sweep algorithm. But instead of line sweep vertically or horiz now set p as the origin, sort the polar angles of the endpoints to p, and sweep counterclockwise. The status queue is built according to how far the intersect segments are to the origin. ontally, we Each time after update of an event, if a segment in the status queue becomes the “top” one, w e will mark it as “visible”. The segments, if never “emerging” at the top of status queue from entering the queue until leaving, will not be counted. In this way, we detect all the visible segments from p.

2.11 and 2.14 two problems can be solved via a modification of the plane-sweep approach. If you are doing this, you should describe the sweep-line status (or its equivalent), the event points, the data structures used for maintaining these, and the actions taken at each type of event point. You should also outline how the desired running time bound follows.

**Assume that you are given a set S of n segments, and consider the plane sweep algorithm to compute all intersection points of S.
How long does it take, in the worst case, to compute all intersections of S, using any algorithm?**

Since every line segment may cross every other line segment, we have Ω(n2) crossing in the worst case, and thus requiring Ω(n2) time to compute.

![image](https://github.com/user-attachments/assets/159d80fd-23dd-4e43-81bc-adbfc75b59ed)

![image](https://github.com/user-attachments/assets/8a1833e8-f581-4086-84bb-72956d785853)












# Polygon Triangulation
## Every simple polygon has a triangulation
## Ever ytriangulation of a simple polygonon n⩾4 vertices contains at least two(triangles that are) ears.
## triangled

![image](https://github.com/user-attachments/assets/d319e05b-70b2-4c20-8e86-760413ea86fe)








![image](https://github.com/user-attachments/assets/b8bf258d-4355-46ce-97bd-c79620739cc5)




**3.3 Prove or disprove: The dual graph of the triangulation of a monotone
polygon is always a chain, that is, any node in this graph has degree at
most two.**
![image](https://github.com/user-attachments/assets/bcf19925-2928-48ca-9a59-5f617c849434)

**Let S be a set of n disjoint triangles in the plane, and let P be a set of m points in the plane.
Design an efficient algorithm to decide, for each point p of P , which triangles from S contains p, if any. What is the
running time of your algorithm?**


**Given a set L of n lines in the plane, give an O(n log n) time algorithm to compute the maximum
level of any vertex in the arrangement A(L)**

**Let S be a set of n points in the plane. Give an O(n2) time algorithm to find the line containing
the maximum number of points in S**


**A rectilinear polygon is a simple polygon of which all edges are horizontal or vertical. Let P be a
rectilinear polygon with n vertices. Give an example to show that ⌊n/4⌋ cameras are sometimes necessary to guard it**

<img width="911" alt="image" src="https://github.com/user-attachments/assets/72a2638e-f7d2-475d-b7c3-6b2feb05fe47" />



**Let P be a simple polygon in the plane and P(P ) be a triangulation of P . Prove that there exists a
3-coloring of the vertices of P such that any triangle in P(P ) has vertices of three different colors**

<img width="956" alt="image" src="https://github.com/user-attachments/assets/2a29a965-8c99-4010-bb4b-b25737fc1af8" />

<img width="956" alt="image" src="https://github.com/user-attachments/assets/dd7e2ad6-9b4c-4856-b196-3ae145eb2b0c" />


**Give the pseudo-code of the algorithm to compute a 3-coloring of a triangulated simple polygon.
The algorithm should run in linear time.**

![image](https://github.com/user-attachments/assets/25c3fb72-d3e9-4668-9e9d-29a484dfe93f)

![image](https://github.com/user-attachments/assets/35a3e310-916c-4240-bbe0-c73c517603a8)

<img width="739" alt="image" src="https://github.com/user-attachments/assets/3ce58a7c-70e4-4e8a-b13c-6ec7c02924e1" />



**Let P be a simple polygon with n vertices, which has been partitioned into monotone pieces. Prove
that the sum of the number of vertices of the pieces is O(n)**


**Let S be a set of n points in the plane. Design an efficient algorithm for computing a triangulation
of P**
<img width="685" alt="image" src="https://github.com/user-attachments/assets/7dfcc522-c31e-4bcb-9458-3687664aaf00" />


**The stabbing number of a triangulated simple polygon P is the maximum number of diagonals
intersected by any line segment interior to P. Give an algorithm that computes a triangulation of a convex polygon
that has stabbing number O(log n).**

A convex polygon P with n vertices, ordered v ​
  in clockwise or counterclockwise order.
  
Balanced Triangulation via Divide and Conquer .This ensures a recursion tree of depth O(logn).A line segment can intersect at most one diagonal per level,
<img width="692" alt="image" src="https://github.com/user-attachments/assets/3cb32c41-f604-452e-976a-cf54aed500b2" />


**Let H be a set of at least three half-planes with a non-empty intersection such that not all bounding
lines are parallel. We call a half-plane h ∈ H redundant if it does not contribute an edge to ∩H. Prove that for any
redundant half-plane h ∈ H there are two half-planes h′, h′′ ∈ H such that h′ ∩ h′′ ⊂ h. Give an O(n log n) time
algorithm to compute all redundant half-planes.**


# LP

**A simple polygon P is called star-shaped if it contains a point q such that for any point p in P
the line segment pq is contained in P. Give an algorithm whose expected running time is linear to decide whether a
simple polygon is star-shaped or not.**
![image](https://github.com/user-attachments/assets/f37c3ce1-be79-4c00-96bf-d81a9495ba77)


The idea is to model the constraints imposed by the polygon's edges as a system of linear inequalities。
Without loss of generality, we assume that the simple polygon P is represented by a counter clockwise chain of its vertices (numbering n) in array form. Given such a chain, it is straightforward to compute the lines representing each edge. Further, these lines can be converted into half-spaces facing the inside of P using orientation primitives.There are n such inequalities (one per edge), forming a system of linear constraints.  **Using a randomized linear programming algorithm**, we achieve the required expected linear time complexity .


<img width="795" alt="image" src="https://github.com/user-attachments/assets/8f47b645-31b1-4f8e-b806-d5edea206ad8" />


**On n parallel railway tracks n trains are going with constant speeds v1, v2, . . . , vn . At time t = 0,
the trains are at positions k1, k2, . . . , kn. Give an O(n log n)-time algorithm that detects all trains that at some moment
in time are leading. To this end, use the algorithm for computing the intersection of half-planes.**

We model the problem in the (t,x)-plane:
Each train's position function x=vit+ki defines a line in the plane.

We are interested in the upper envelope of these lines, i.e., the set of all points (t,x) such that x≥v 
it+ki for all i

Use an efficient algorithm to compute the intersection of these n half-planes in 2D. This results in a convex polygonal region (possibly unbounded). The boundary of this region is the upper envelope of the lines.

Traverse the boundary of the convex region. Each edge of the boundary corresponds to a line from the original set of trains. Collect all such lines.The trains whose lines appear on the boundary are the ones that are leading at some time.



# 5 Range search

## K-d tree

as K-D tree need  presort operator,so kd-tree for a set of n points uses O(n) storage and can be con
structed
in O(nlogn) time.

A kd-tree for a set P of n points in the plane uses O(n) storage
and can be built in O(nlogn) time. A rectangular range query on the kd-tree
*
takes O(n+k) time, where k is the number of reported points

## range tree

range tree, which has a better query time, namely O(log2n+k). The
price we have to pay for this improvement is an increase in storage from
O(n) for kd-trees to O(nlogn) for range trees.


**5.2 Describe algorithms to insert and detele points from a kd-tree.In your algorithm you do not need to take care of rebalancing the structure**

For insertion,start at the root and compare the point's coordinate in the current splitting dimension. If it's less than the node's value, go left; otherwise, go right. 
Continue this recursively until  finding a null spot where you can add the new node.
just finding the correct path based on the splitting dimensions and adding the new node as a leaf or internal node where appropriate.

Deletion ,the node to delete is a leaf, it's simple—just remove it.



**5.6 Describe algorithms to insert and detele points from a range tree.In your algorithm you do not need to take care of rebalancing the structure**

insert in the main tree,do binary search at every nodes. for all the effected parents,walk back and do binary search on y coordinates.


### (5.8)Theorem 5.8 showed that a range tree on a set of n points in the plane requires O(nlogn) storage. One could bring down the storage requirements by storing associated structures only with a subset of the nodes in the main tree.

a. Suppose that only the nodes with depth 0, 2, 4, 6, . . . have an associated
structure. Show how the query algorithm can be adapted to answer
queries correctly.

When visiting a node with an associated structure (depth even), use it to get all points in the desired y-range.

When visiting a node without associated structure (depth odd), recursively visit both children to simulate the missing structure.

b. Analyze the storage requirements and query time of such a data structure.

nlogn/2

squar(logn)

c. Suppose that only the nodes with depth 0, 1/j
logn., 2/j
logn., . . . have
an associated structure, where "j "  is a constant. Analyze the storage
requirements and query time of this data structure. Express the bounds
in n and j**

storage:j times n

query:2^(1/j logn) squar(logn)

![image](https://github.com/user-attachments/assets/8fa8decd-82cb-4330-9b5c-378c12658ca6)

### 5.9 One can use the data structures described in this chapter to determinewhether a particular point (a,b) is in a given set by performing a range query with range [a : a]×[b : b].

a. Prove that performing such a range query on a kd-tree takes time
O(logn).

O(n)=O(1)+O(n/2)

b. What is the time bound for such a query on a range tree? Prove your
answer.

O(logn)

**5.10 In some applications one is interested only in the number of points that
lie in a range rather than in reporting all of them. Such queries are often
referred to as range counting queries. In this case one would like to avoid
having an additive term of O(k) in the query time.**

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


**5.11 Let S1 be a set of n disjoint horizontal line segments and let S2 be a set
of m disjoint vertical line segments. Give a plane-sweep algorithm that
counts in O((n+m) log(n+m)) time how many intersections there are
in S1 /S2.**

![image](https://github.com/user-attachments/assets/8d268526-64a7-4a4d-a1ff-c5bf536f0124)

![image](https://github.com/user-attachments/assets/a55f8d41-7556-4097-9079-1e0f44bc8f86)
![image](https://github.com/user-attachments/assets/370bbdac-58aa-43e6-9c41-a12e0da37591)







# 6 Point Location 

## trapezoidal map
more general method of defining a subdivision of the plane into simple regions
![image](https://github.com/user-attachments/assets/4bc7518c-f858-4ad0-b4d0-e99f93474b29)

![image](https://github.com/user-attachments/assets/f80f43ba-412b-4a01-a665-619e0802fc65)

### construction ： randomized incremental algorithm

We could construct the trapezoidal map easily by plane sweep.
![image](https://github.com/user-attachments/assets/0784fab8-37de-4a99-9434-640a086dc082)


**6.4 Show that, given a planar subdivision S with n vertices and edges and a query point q, the face of
S containing q can be computed in time O(n). Assume that S is given in a doubly-connected edge list.**

<img width="854" alt="image" src="https://github.com/user-attachments/assets/16f2a0f4-b378-44cb-ab12-318437f61b8e" />




**（6.5） Given a convex polygon P as an array of its n vertices in sorted order along the boundary. Show
that, given a query point q, it can be tested in time O(log n) whether q lies inside P**
For a convex polygon, if you fix one vertex (e.g. P[0]), the polygon can be split into n - 2 non-overlapping triangles
If you can find the triangle that might contain the query point q, and test if it lies within that triangle, you can determine if q is inside the polygon.

Choose a fixed anchor vertex: Let’s take P[0].
	2.	Binary Search between vertices P[1] to P[n-1] to find the triangle \triangle(P[0], P[i], P[i+1]) such that q lies within the wedge formed by P[0]P[i] and P[0]P[i+1].
Use the orientation test (cross product) to determine:
	•	If q lies to the left or right of the vector from P[0] to P[i].
	3.	Once the correct triangle is found in O(\log n), test if q lies inside the triangle \triangle(P[0], P[i], P[i+1]) using three orientation tests.
 
**（6.6）Given a y-monotone polygon P as an array of its n vertices in sorted order along the boundary.
Can you generalize the solution to the previous exercise to y-monotone polygons?**


**（6.8）Design a deterministic algorithm, that is, one that does not make random choices, to compute the
trapezoidal map of a set of non-crossing line segments. Use the plane sweep paradigm from Chapter 2. The worst-case
running time of the algorithm should be O(n log n)**

![image](https://github.com/user-attachments/assets/263b4007-44d2-450f-955e-a6cb72ab9e5e)


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
![image](https://github.com/user-attachments/assets/b47ae2fa-4800-45c1-9203-a9ba29877e50)

![image](https://github.com/user-attachments/assets/4c1dedc8-4dae-44f8-8d45-f2fc3dcc0c7d)

![image](https://github.com/user-attachments/assets/0e8b334c-266d-4d1d-9bdd-854886c94389)


## Give an example of a set of n line segments and the order on them that makes the randomized trapezoidal algorithm create a search structure of size Θ(n2) and having query time Θ(n), in the worst case.

![image](https://github.com/user-attachments/assets/fdb6c7a1-2438-487e-8355-348c9254b4ec)


# Voronoi Diagrams
A Voronoi diagram encodes proximity information, that is, what is close to what.

![image](https://github.com/user-attachments/assets/9862dcf3-b1cf-4930-8252-561bd6833e4b)

## Voronoi Diagrams Properties 
Each Voronoi region V(pi) is convex. Could be  bounded or unbounded.

A Voronoi vertex has at least three nearest  neighbors 
## Computing the Voronoi Diagram
plane sweep algorithm O(nlogn)

the problem of sorting n real numbers
is reducible to the problem of computing Voronoi diagrams, so any algorithm for computing Voronoi diagrams must take
"(nlogn) time in the worst case

**What is the complexity of the Voronoi diagram of any set P of n points in the plane, using O notation, assuming
no four points of P lie on a same circle?**
O(n)

**Given a set P of n points in the plane, what is the maximum number of edges in P s Voronoi diagram?**
3n-6

**7.1Prove that for any n > 3 there is a set of n point sites in the plane such that one of the cells of
Vor(P ) has n − 1 vertices.**


placing n−1 points equally spaced on a circle around a central point would result in the central Voronoi cell being a regular (n−1)-gon with n−1 vertices

**7.3Prove that any algorithm for computing the Voronoi diagram of a set of n point sites in the plane
needs Ω(n log n) in the worst-case.**

use a reduction from the sorting problem，which is known to have a lower bound of Ω(nlogn) 

or by contra

suppose faster than Ω(n log n)




**7.10Let P be a set of n points in the plane. Give an O(n log n) time algorithm to find two points in P
that are closest together**

keep the minmum

![image](https://github.com/user-attachments/assets/47e89ed7-44da-4219-8994-7c937c0681cd)



**7.11Let P be a set of n points in the plane. Give an O(n log n) time algorithm to find for each point p
in P another point in P that is closest to it.**
The Voronoi diagram for n points can be built in O(n \log n) time.

The total number of Voronoi neighbor checks across all n points is bounded by the number of Voronoi edges, which is O(n).
![image](https://github.com/user-attachments/assets/8b55958b-6c8e-43f3-bf33-7bb9192eb2a2)


**（7.13）Let the Voronoi diagram of a point set P be stored in a doubly-connected
edge list inside a bounding box. Give an algorithm to compute all points
of P that lie on the boundary of the convex hull of P in time linear in the
output size. Assume that your algorithm receives as its input a pointer to
the record of some half-edge whose origin lies on the bounding box.**

Acellof theVoronoidiagramisunboundedifandonlyif thecorresponding site lies on the convex hull. (Observe that a site is on the convex hull if and only if it is the closest point from some point at infinity.) Thus, given a Voronoi diagram, it is easy to extract the convex hull in linear time.

Start at a half-edge e on the bounding box.

Traverse the outer face by following next pointers until returning to e.

For each edge h in this cycle:
Get the site p from h’s incident face.
Add p to the result list if not already present.

The outer face (bounding box) forms a single cycle in the DCEL. Traversing this cycle ensures all unbounded Voronoi edges (and thus convex hull points) are visited 

Each convex hull point's Voronoi cell touches the bounding box exactly once



# Arrangements and Duality
k-level = Parts of the lines/curves with exactly k other lines above.

0-level = Upper envelope


![image](https://github.com/user-attachments/assets/d80b1d73-cc5a-42d6-bc93-044052dbbed1)


**8.3Use Euler’s formula to show that the maximum number of faces is n2/2+n/2+1 in an arrangement
with n(n − 1)/2 vertices and n2 edges.**




**8.4Let L be a set of n lines in the plane. Give an O(n log n) time algorithm to compute an axis-parallel
rectangle that contains all the vertices of A(L) in its interior.**

sort the line by slope

<img width="809" alt="image" src="https://github.com/user-attachments/assets/239f3fd5-3362-4d22-8f34-0e88e7ffbb75" />

**8.7Let R be a set of n red points in the plane, and let B be a set of n blue
points in the plane. We call a line ℓ a separator for R and B if ℓ has
all points of R to one side and all points of B to the other side. Give a
randomized algorithm that can decide in O(n) expected time whether R
and B have a separator.**
<img width="887" alt="image" src="https://github.com/user-attachments/assets/f2f46103-449b-432f-8baf-9c3ff10ca243" />





**8.13Given a set L of n lines in the plane, give an O(n log n) time algorithm to compute the maximum
level of any vertex in the arrangement A(L)**

Sort lines by slope.O(n \log n)

Compute the upper envelope of the lines.

**8.14 Let S be a set of n points in the plane. Give an O(n2) time algorithm to find the line containing
the maximum number of points in S**

by using dual properties :	Find a point where the maximum number of dual lines intersect.

There are O(n^2) pairs of lines.
	•	For each pair, checking how many other lines go through the same point costs O(n).
	•	Naively, this would be O(n^3), but we optimize:

Instead:
	•	Store intersection points and counts in a hash map.
	•	Each of the O(n^2) pairs produces a point — insert into the map and increment its count.



**8.15 Let S be a set of n segments in the plane. We want to preprocess S into a
data structure that can answer the following query: Given a query line !,
how many segments in S does it intersect?
a. Formulate the problem in the dual plane.
b. Describe a data structure for this problem that uses O(n2) expected
storage and has O(logn) expected query time.
c. Describe how the data structure can be built in O(n2 logn) expected
time.**

(a) Each segment in the primal corresponds to a strip (region) in the dual

(b)

(c)


# Reference
https://www.cs.cmu.edu/afs/cs/academic/class/15456-f15/Handouts/cmsc754-lects.pdf



