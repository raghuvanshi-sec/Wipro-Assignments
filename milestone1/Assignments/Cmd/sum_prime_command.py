import sys

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

total = 0

for i in range(1, 11):
    num = int(sys.argv[i])

    if is_prime(num):
        total += num

print("Sum of Prime Numbers =", total)