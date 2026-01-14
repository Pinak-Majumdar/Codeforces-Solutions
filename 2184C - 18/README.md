We are given two integers n and k for each test case. The task is to find the minimum number of times we must repeatedly divide n by 2 (taking the ceiling when needed) until we reach exactly k, if possible. If it is not possible, we output -1.

To do this, we start with a counter t equal to zero. On each step we increase t by one and compute two values: low and high. These represent the range of values that n could become after t divisions by two. low is the standard integer division of n by two to the power t. high is the ceiling division of n by two to the power t, which means that if n is not exactly divisible by 2 to the power t then high is one more than low.

If either low or high matches k exactly, we output t, because we have found the minimum number of steps needed. If high is less than k, or if high becomes zero before k is reached, then it is not possible to ever reach k by repeated division, and we print -1.

This approach works because repeated division by two shrinks the number and produces a range of possible values at each step. Checking both the floor and ceiling values allows us to cover the integer values that can arise from such division.