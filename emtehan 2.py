def is_prime(number):
    if number < 2:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i = i + 1
    return True

def find_kth_prime_after_n(n, k):
    count = 0
    current = n + 1
    result = 0

    while result == 0:
        if is_prime(current):
            count = count + 1
            if count == k:
                result = current
        current = current + 1

    print("The", k, "th prime number after", n, "is:", result)

n = 1500000
k = 4

find_kth_prime_after_n(n,k)