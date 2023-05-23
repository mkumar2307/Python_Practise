'''
you are given N fractions numbered from 0 to N-1. your task is to count the number of occurrences of the fraction that appears most often.
Notice that two fractions may be equal even if they have different representations; for example 3/5 and 6/10 are equal.
you should not assume that floating point operations are precise.
write a function : def solution(x,y) that give two arrays x and y consisting of N integers each  which represents the K-th fraction as x[K]/y[K] returns the number of occurrences of the fraction that appears most often.
'''
def solution(x, y):
    fraction_count = {}  # Dictionary to store counts of fractions
    max_count = 0  # Variable to keep track of the maximum count

    # Iterate over the fractions
    for i in range(len(x)):
        # Calculate the greatest common divisor (GCD) of x and y using the compute_gcd function
        gcd = compute_gcd(x[i], y[i])

        # Reduce the fraction by dividing both numerator and denominator by GCD
        reduced_x = x[i] // gcd
        reduced_y = y[i] // gcd

        # Create a tuple representing the reduced fraction
        fraction = (reduced_x, reduced_y)

        # Increment the count for the fraction in the dictionary
        fraction_count[fraction] = fraction_count.get(fraction, 0) + 1

        # Update the maximum count if necessary
        if fraction_count[fraction] > max_count:
            max_count = fraction_count[fraction]

    return max_count


def compute_gcd(a, b):
    # Calculate the greatest common divisor (GCD) using the Euclidean algorithm
    while b:
        a, b = b, a % b
    return a
