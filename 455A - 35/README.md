We count the frequency of each number and use dynamic programming to decide whether to take or skip each value. Taking a value gives points equal to the value multiplied by its frequency but prevents taking adjacent values. For each number, we choose the option that maximizes the total score. The final DP value gives the answer.

