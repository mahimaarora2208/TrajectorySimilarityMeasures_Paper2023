import math

T1 = [(1,1),(3,4),(4,0),(6,2),(7,1)]
T2 = [(1,5),(1,2),(3,2),(5,3),(8,3),(8,5)]

def pointDistance(p1, p2):
    dist = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    return dist

def dynamicTimeWarpingDistance(T1, T2):
    m, n = len(T1), len(T2)
    if m == 0 and n == 0:
        return 0    
    if m == 0 or n == 0:
        return math.inf
    
    




dynamicTimeWarpingDistance(T1, T2)
