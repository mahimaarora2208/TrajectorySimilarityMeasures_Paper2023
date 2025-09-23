import math
'''
    * Longest common sub sequence(LCSS) distance between two trajectories T1 and T2 is defined as the size of longest common sub sew between two trajectories.
    * It works on a threshold where if dis(p1,p2) <= Threshold, then p1 and p2 are a match pair.
    * LCSS distance finds ALL match pairs. It is a non-metric and sensitive to noise as compared to Euclidean Distance metric.
'''
T1 = [(1,1),(3,4),(4,0),(6,2),(7,1)]
T2 = [(1,5),(1,2),(3,2),(5,3),(8,3),(8,5)]
memo = {}
THRESHOLD = 1

def pointDistance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


def longestCommonSubseq(T1, T2):
    m, n  = len(T1), len(T2)
    # base case
    print("m: ", m, " n: ", n)
    if m == 0 or n == 0:
        return 0
    else:
        print("Threshold compare: ", pointDistance(T1[-1], T2[-1]))
        if pointDistance(T1[-1], T2[-1]) <= THRESHOLD:
            dist = 1 + longestCommonSubseq(T1[:-1], T2[:-1])
            print("Distance: ",  dist)
        else:
            dist = max(longestCommonSubseq(T1[:-1], T2), longestCommonSubseq(T1, T2[:-1]))
            print("Distance_else: ", dist)  
    print(dist)

longestCommonSubseq(T1,T2)
        
    