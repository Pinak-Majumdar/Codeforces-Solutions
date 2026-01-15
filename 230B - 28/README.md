For each number, we need to determine whether it is a T-prime. A T-prime is a number that has exactly three positive divisors. This happens only when the number is a square of a prime number.

To check this, we first take the square root of the number. If the square root is not an integer, then the number cannot be a T-prime. If the square root is less than 2, it is also invalid.

If the square root is an integer, we then check whether this square root itself is a prime number. This is done by testing divisibility up to the square root of that value.

If both conditions are satisfied, the number is a T-prime and we print YES. Otherwise, we print NO.

This approach is efficient and works within the given constraints.