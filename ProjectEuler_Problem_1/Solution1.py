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
