# TrajectorySimilarityMeasures_Paper2023

This repository implements non-learning based measures which computes trajectory similarity in free space. This includes point-based measures which are widely used to compute the similarity among trajectories consisting of sampling points.

## Euclidean Distance Metric
    * Requires length of both trajectories to be same
    * Distance sum is calculated from T1[i] and T2[i] meaning at same time, where are each trajectory points.
    * Parameter free measure with TC as O(n)

## Dynamic Time Warping Distance (DTW)
    * DTW or dynamic time warping is similar to ED but it can deal with different length trajectories AND can align one point iwth mroe consecutive points of another trajectory.
    * It is a non-metric and is most commonly used for similarity computation. 

## Longest Common Subsequence Distance (LCSS)
    * Longest common sub sequence(LCSS) distance between two trajectories T1 and T2 is defined as the size of longest common sub sew between two trajectories.
    * It works on a threshold where if dis(p1,p2) <= Threshold, then p1 and p2 are a match pair.
    * LCSS distance finds ALL match pairs. It is a non-metric and sensitive to noise as compared to Euclidean Distance metric.

## Edit Distance on Real Sequence (EDR)
    * 