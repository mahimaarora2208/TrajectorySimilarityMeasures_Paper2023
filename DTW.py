import math
''' 
    * DTW or dynamic time warping is similar to ED but it can deal with different length trajectories AND can align one point iwth mroe consecutive points of another trajectory.
    * It is a non-metric and is most commonly used for similarity computation. 
'''
T1 = [(1,1),(3,4),(4,0),(6,2),(7,1)]
T2 = [(1,5),(1,2),(3,2),(5,3),(8,3),(8,5)]
memo = {}

def pointDistance(p1, p2):
    dist = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    return dist

def dynamicTimeWarpingDistance(T1, T2):
    m, n = len(T1), len(T2)
    if m == 0 and n == 0:
        return 0    
    elif m == 0 or n == 0:
        return math.inf
    else:
       if (tuple(T1),tuple(T2)) not in memo.keys():
        dist = pointDistance(T1[-1], T2[-1]) + min(dynamicTimeWarpingDistance(T1[:-1], T2), dynamicTimeWarpingDistance(T1, T2[:-1] ),
                                          dynamicTimeWarpingDistance(T1[:-1], T2[:-1]))
        memo[(tuple(T1),tuple(T2))] = dist
       else:
        return memo[(tuple(T1),tuple(T2))]
    print(dist)
    return dist

dynamicTimeWarpingDistance(T1, T2)
