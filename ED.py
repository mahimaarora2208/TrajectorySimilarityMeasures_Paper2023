import math
'''
Euclidean Distance Metric for point based measures
    * Requires length of both trajectories to be same
    * Distance sum is calculated from T1[i] and T2[i] meaning at same time, where are each trajectory points.
    * Parameter free measure with TC as O(n)
'''
T1 = [(1,1),(3,4),(4,0),(6,2),(7,1)]
T2 = [(1,5),(1,2),(3,2),(5,3),(8,3)]

def pointDistance(p1, p2):
    dist = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    return dist


def TrajectoryDistance(T1, T2):
    totalSum = 0
    if len(T1) != len(T2):
        raise ValueError("Trajectories must have same lengths!")
    for i in range(len(T1)):
        distance = pointDistance(T1[i],T2[i])
        totalSum += distance
    ED = totalSum/len(T1)
    print(round(ED, 2))


TrajectoryDistance(T1, T2)
