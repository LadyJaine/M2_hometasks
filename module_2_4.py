numbers_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes_ = []
not_primes_ = []
for x in numbers_:
    is_prime = True
    for j in range(2,x):
        if x % j == 0:
            is_prime = False
            break
    if is_prime:
        primes_.append(x)
    else:
        not_primes_.append(x)
print(primes_,not_primes_)
