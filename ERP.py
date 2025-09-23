import math
'''
    * ERP or edit distance with real penalty is also an edit-distance based measure but it IS a metric unlike EDR and DTW which are non-metric.
    * This is a metric that can be used for indexing and pruning.
    * ERP does NOT require a threshold parameter but a reference point i.e. gap point. 
    TC is O(mn) where m = len(T1) and n = len(T2)

'''

T1 = [(1,1),(3,4),(4,0),(6,2),(7,1)]
T2 = [(1,5),(1,2),(3,2),(5,3),(8,3),(8,5)]
REFERENCE_POINT = (3,2)

def pointDistance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def editDistanceWithRealPenality(T1, T2):
    m, n = len(T1), len(T2)
    # base cases
    if m == 0 and n == 0:
        return 0
    if m == 0:
        dist = 0
        for i in range(n):
            dist += pointDistance(T2[i], REFERENCE_POINT)
        return dist
    elif n == 0:
        dist = 0
        for i in range(m):
            dist += pointDistance(T1[i], REFERENCE_POINT)
        return dist
    else:
        dist = min(editDistanceWithRealPenality(T1[:-1], T2[:-1]) + pointDistance(T1[-1], T2[-1]),
                   editDistanceWithRealPenality(T1, T2[:-1]) + pointDistance(T2[-1], REFERENCE_POINT),
                   editDistanceWithRealPenality(T1[:-1], T2) + pointDistance(T1[-1],REFERENCE_POINT))
    return dist

dist = editDistanceWithRealPenality(T1, T2)
print(round(dist,2))