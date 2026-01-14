We are given a string consisting of characters u and n. The task is to find the minimum number of deletions required so that no two remaining u characters are too close to each other.

First, we count the total number of u characters in the string. Then, we decide how many u characters we are allowed to keep.

We iterate through the string while keeping track of the last position where a u was kept. A u can be kept only if it is at least two positions away from the previously kept u. This greedy choice ensures that the remaining u characters are spaced out as much as possible.

By doing this, we maximize the number of u characters that can remain without violating the condition. The answer is then the total number of u characters minus the number of u characters we kept.

This approach runs in linear time and works efficiently for all valid inputs.