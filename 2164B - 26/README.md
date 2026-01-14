We are given an array and need to find any pair of elements l[i] and l[j] with i < j such that the remainder of l[j] divided by l[i] is even.

To solve this, we check all possible pairs of indices i and j where i comes before j. For each pair, we compute l[j] % l[i] and check whether it is even. As soon as we find a pair that satisfies this condition, we print the two elements and stop searching for that test case.

If no such pair exists after checking all pairs, we print -1.

This approach works because only one valid pair is required, and the constraints are small enough for a brute-force solution to run within the time limits.