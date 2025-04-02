import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def brute_force(points):
    min_dist = float('inf')
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
    return min_dist

def closest_pair(Px, Py):
    n = len(Px)
    if n <= 3:
        return brute_force(Px)
    
    mid = n // 2
    mid_x = Px[mid].x
    
    left_Px = Px[:mid]
    right_Px = Px[mid:]
    
    left_Py = []
    right_Py = []
    for p in Py:
        if p.x <= mid_x:
            left_Py.append(p)
        else:
            right_Py.append(p)
    
    delta_left = closest_pair(left_Px, left_Py)
    delta_right = closest_pair(right_Px, right_Py)
    delta = min(delta_left, delta_right)
    
    # Merge left_Py and right_Py to get merged_Py sorted by y
    merged_Py = []
    i = j = 0
    while i < len(left_Py) and j < len(right_Py):
        if left_Py[i].y <= right_Py[j].y:
            merged_Py.append(left_Py[i])
            i += 1
        else:
            merged_Py.append(right_Py[j])
            j += 1
    merged_Py += left_Py[i:]
    merged_Py += right_Py[j:]
    
    # Create the strip
    strip = [p for p in merged_Py if abs(p.x - mid_x) < delta]
    
    # Check the strip
    delta_strip = delta
    for i in range(len(strip)):
        for j in range(i+1, min(i+6, len(strip))):
            d = distance(strip[i], strip[j])
            if d < delta_strip:
                delta_strip = d
    
    return min(delta, delta_strip)

def closest_pair_main(points):
    Px = sorted(points, key=lambda p: p.x)
    Py = sorted(points, key=lambda p: p.y)
    return closest_pair(Px, Py)
