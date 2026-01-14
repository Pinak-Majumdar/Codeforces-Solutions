For a number X to be coprime with all elements of the array, it is sufficient for X to be coprime with the GCD of the entire array.
This is because any common divisor of X and an array element must also divide the array’s GCD.
So, we first compute the GCD of all elements. Then, starting from X=2, we find the smallest integer such that gcd(X,array_gcd)=1.
That value of X is guaranteed to be coprime with every element in the array.

The solution runs efficiently since the GCD is computed once per element.