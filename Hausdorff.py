import math
'''
    * Hausdorf distance is a metric measure which measures the maximum distance of all distance values from a point of one trajectory to the nearest point in another trajectory. 
    * TC is O(mn) where m = len(T1) and n = len(T2)
    * Parameter free measure meaning no threshold or reference point parameter is needed.
    * This distance does NOT consider direction of two trajectories.

'''

T1 = [(1,1),(3,4),(4,0),(6,2),(7,1)]
T2 = [(1,5),(1,2),(3,2),(5,3),(8,3),(8,5)]

def pointDistance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def hausdorffDistance(T1, T2):
    m, n = len(T1), len(T2)
    minDistT1 = []
    minDistT2 = []
    for i in T1:
        minDist = math.inf
        for j in T2:
            minDist = min(minDist, pointDistance(i,j))
        minDistT1.append(round(minDist,2))

    for i in T2:
        minDist = math.inf
        for j in T1:
            minDist = min(minDist, pointDistance(i,j))
        minDistT2.append(round(minDist,2))    

    return max(max(minDistT1), max(minDistT2))

dist = hausdorffDistance(T1, T2)
print(dist)