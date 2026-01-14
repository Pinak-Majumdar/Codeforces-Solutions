We are given an array of integers and want to maximize the total sum after performing at most one special operation. The special operation allows us to choose any contiguous subarray and add a value to every element in that subarray such that all modified values become equal to the maximum element of that range originally.

The first step is to calculate the sum of all elements in the array. That sum is the baseline if we do not perform any operation.

To determine the best possible increase, we define a new value for each index based on the formula 2 * (i + 1) - a[i], where i is the index (starting from 0) and a[i] is the element at that index. This transforms the problem into finding a maximum subarray sum of this transformed array. This can be done using a running maximum similar to Kadane’s algorithm: at each position we either start a new segment or extend the current one, and we keep track of the best segment sum seen so far.

The final answer for each test case is the baseline sum plus the maximum increase found. If all increases are negative or zero, the baseline sum remains the answer.