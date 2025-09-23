import math
'''
    * Frechet distance is a non-metric measure which considers direction of two trajectories unlike Hausdorff.
    * This is sensitive to noises.
    * Frechet distance between two trajectories of man and dog is the shortest length of the leash required. 
    * TC is O(mn) where m = len(T1) and n = len(T2)
    * Frechet can be ametric by using "discrete frechet distance" 

'''

T1 = [(1,1),(3,4),(4,0),(6,2),(7,1)]
T2 = [(1,5),(1,2),(3,2),(5,3),(8,3),(8,5)]


def pointDistance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def frechetDistance(T1, T2):
    m, n = len(T1), len(T2)
    # Base case
    if n == 1:
        maxDist = -1
        for i in T1:
            maxDist = max(maxDist, pointDistance(i ,T2[0]))
        return maxDist
    elif m == 1:
        maxDist = -1
        for i in T2:
            maxDist = max(maxDist, pointDistance(i ,T1[0]))
        return maxDist
    else:
        dist = max(pointDistance(T1[-1], T2[-1]), min(frechetDistance(T1, T2[:-1]), frechetDistance(T1[:-1], T2), frechetDistance(T1[:-1], T2[:-1])))

    return dist

dist = frechetDistance(T1, T2)
print(round(dist,2))