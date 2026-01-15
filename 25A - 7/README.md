We are given a list of integers where all numbers except one have the same parity. The task is to find the position (1-based index) of the number whose parity is different from the rest.

To solve this, we iterate through the list and separate the indices of odd numbers and even numbers into two lists. Since the problem guarantees that exactly one number is different, one of these lists will have length 1.

If the list of odd indices has length 1, then that index is the answer. Otherwise, the single even index is the answer.

This approach works in linear time and is sufficient given the constraints.