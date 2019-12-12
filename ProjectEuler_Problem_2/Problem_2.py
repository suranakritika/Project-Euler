# imports
import math

# Function
def fib(index):
    term1 = pow(1.618034,i)
    term2 = pow(-0.618034,i)
    fibonacci=(term1-term2)//math.sqrt(5)
    return fibonacci
    
# Main
n=input()
i=0
s=0
while True:
    i+=3
    print(fib(i))
    s+=fib(i)
    if(fib(i)>n):
        s-=fib(i)
        print(n)
        print(int(s))
        break
