''' 14. Determine the n-th element of the sequence 1,2,3,2,2,5,2,2,3,3,3,7,2,2,3,3,3,... obtained from the sequence of natural numbers by replacing composed numbers 
with their prime divisors, each divisor d being written d times, without memorizing the elements of the sequence. '''
# Problem no. 14
import math

def prime_divisors(n):
    divisors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            divisors.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        divisors.append(n)
    return divisors

n = int(input("Enter n: "))

count = 0
num = 1

while True:
    if num == 1 or all(num % d != 0 for d in range(2, int(math.sqrt(num)) + 1)):
        count += 1
        if count == n:
            print(f"The {n}-th element is {num}.")
            break
    else:
        for p in prime_divisors(num):
            for _ in range(p):
                count += 1
                if count == n:
                    print(f"The {n}-th element is {p}.")
                    exit()
    num += 1
