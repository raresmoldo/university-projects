# 5.Generate the largest prime number smaller than a given natural number n. If such a number does not exist, a message should be displayed.
# Problem no.5
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter a natural number n: "))

# Look for the largest prime smaller than n
for candidate in range(n - 1, 1, -1):
    if is_prime(candidate):
        print(f"The largest prime number smaller than {n} is {candidate}.")
        break
else:
    print(f"There is no prime number smaller than {n}.")
