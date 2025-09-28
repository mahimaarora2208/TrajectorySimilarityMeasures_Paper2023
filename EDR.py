import math
'''
    * EDR is one of the "edit-distance" based measures similar to LCSS. Edit distance equals to no. of necessary operations e.g. insertion, deletion and replacement when TRANSFORMING one trajectory to another.
    * EDR is different from LCSS by setting a "cost" paprameter to measure cost of unmatched pair of points.
    * TC is O(mn) where m = len(T1) and n = len(T2)
'''

T1 = [(1,1),(3,4),(4,0),(6,2),(7,1)]
T2 = [(1,5),(1,2),(3,2),(5,3),(8,3),(8,5)]
THRESHOLD = 1
memo = {}

def pointDistance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def editDistanceOnRealSequence(T1, T2):
    m, n = len(T1), len(T2)
    # base cases
    if m == 0:
        return n
    elif n == 0:
        return m
    else:
        # calculate cost
        if pointDistance(T1[-1], T2[-1]) <= THRESHOLD:
            cost = 0
        else:
            cost = 1
        if (tuple(T1),tuple(T2)) not in memo.keys():
            dist = min(editDistanceOnRealSequence(T1[:-1], T2) + 1,
            editDistanceOnRealSequence(T1, T2[:-1]) + 1,
            editDistanceOnRealSequence(T1[:-1], T2[:-1]) + cost) 
            memo[(tuple(T1), tuple(T2))] = dist
        else:
            return memo[(tuple(T1),tuple(T2))]
    return dist
        

dist = editDistanceOnRealSequence(T1, T2)
print(dist)

