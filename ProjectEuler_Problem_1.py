# Problem 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


T = int(input())
for _ in range(T):
    N = int(input())
    multiples_of_3 = (N - 1) // 3
    multiples_of_5 = (N - 1) // 5
    multiples_of_15 = (N - 1) // 15
    sum = (3 * multiples_of_3 * (multiples_of_3 + 1) // 2
           + 5 * multiples_of_5 * (multiples_of_5 + 1) // 2
           - 15 * multiples_of_15 * (multiples_of_15 + 1) // 2)
    print(sum)
