# Problem 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


T = int(input())
for _ in range(T):
    N = int(input())
    N3 = (N - 1) // 3
    N5 = (N - 1) // 5
    N15 = (N - 1) // 15
    sum = (3 * N3 * (N3 + 1) // 2
           + 5 * N5 * (N5 + 1) // 2
           - 15 * N15 * (N15 + 1) // 2)
    print(sum)
