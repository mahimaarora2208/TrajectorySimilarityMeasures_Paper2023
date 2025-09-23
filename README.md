# TrajectorySimilarityMeasures_Paper2023

This repository implements non-learning based measures which computes trajectory similarity in free space. This includes point-based measures which are widely used to compute the similarity among trajectories consisting of sampling points.

## Euclidean Distance Metric
    * Requires length of both trajectories to be same
    * Distance sum is calculated from T1[i] and T2[i] meaning at same time, where are each trajectory points.
    * Parameter free measure with TC as O(n)

## Dynamic Time Warping Distance (DTW)