primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

arr = [1,2,3]
prime_check = dict()
result = 1
for num in arr:
    if num == 1:
        continue
    for prime in primes:
        if num < prime:
            break
        else:
            if not num%prime:
                for i in range(1, 8):
                    if num%(prime**i):
                        if not prime in prime_check.keys():
                            prime_check[prime] = i-1
                        else:
                            if prime_check[prime] < i-1:
                                prime_check[prime] = i-1
                        break
for num in prime_check.keys():
    result *= num**prime_check[num]
print(result)