We are given three integers s, k, and m for each test case. The goal is to maximize the number of units of sand left in the upper half of an hourglass at a certain time.

The idea is to compute how many full intervals of k fit into m, which we call f. Each full interval corresponds to flipping the hourglass. The current state after these flips determines how much sand can remain in the upper half. If the number of flips is even, we can use all of the sand s. If the number of flips is odd, the sand that stays in the upper half is limited by the minimum of s and k.

We also have a remainder t, which is m modulo k. Because t minutes have already passed in the current interval, that many units of effective sand are lost.

The answer is the remaining sand after accounting for these intervals and the remainder. This approach runs in constant time for each test case and handles the constraints efficiently.