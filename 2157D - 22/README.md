For each test case, we are given an array and a range [l, r]. We need to choose a value m within this range such that the total sum of absolute differences between m and all array elements is minimized.

A known property is that the sum of absolute differences is minimized when m is the median of the array. So, we first sort the array and take the middle element as the median.

However, m must lie within the range [l, r]. If the median is smaller than l, we set m to l. If the median is larger than r, we set m to r. Otherwise, we keep the median as it is.

Once m is fixed, we compute the sum of absolute differences between each array element and m, and output the result.

This approach works efficiently because sorting allows us to find the median, and the rest of the computation is linear.