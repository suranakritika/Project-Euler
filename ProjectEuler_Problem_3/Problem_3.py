# Code

import math
prime = 0
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    while n % 2 == 0: 
        prime = 2
        n /= 2 
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            prime = i 
            n /= i 
    if n > 2: 
        prime = n
    print(int(prime))
