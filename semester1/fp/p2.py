# 8. Find the smallest number m from the Fibonacci sequence, defined by f[0]=f[1]=1, f[n]=f[n-1] + f[n-2], for n > 2, larger than the given natural number n. (e.g. for n = 6, m = 8).
# Problem no. 8
n = int(input("Enter a natural number n: "))


f1, f2 = 1, 1
while f2 <= n:
    f1, f2 = f2, f1 + f2

print(f"The smallest Fibonacci number larger than {n} is {f2}.")
