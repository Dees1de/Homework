numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    a = 0
    for j in range(len(numbers)):
        if (i+1) % (j+1) == 0:
            a = a + 1
        if a > 2:
            not_primes.append(i+1)
            break
    if a == 2:
        primes.append(i+1)
print('Простые числа: ', primes)
print('Не простые числа: ',not_primes)