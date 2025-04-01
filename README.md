# computational-geometry

## Closest-Pair problem
closest pair could be one from the left half, one from the right half, or the minimum of the two closest pairs from each half

### divide and conquer approach

1.Sort the points by their x-coordinates.

2.Divide the sorted list into two halves.

3.Recursively find the closest pair in each half.

4.Combine the results by checking for pairs that cross the two halves

by examining points within a **vertical strip** around the dividing line. This strip is checked efficiently by considering only points within a certain y-coordinate range.
