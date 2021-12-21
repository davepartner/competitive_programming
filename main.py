# check if a number is a prime number

# any number that can only be divided by 1 and itself
# brute

# prime number = 2 - (prime_number - 1)
# 2 - 9999
# 10000/3

# first code : 735 seconds
# second code : 387 seconds
# third code:   219 seconds
# number = x * n
# 10 = 2 * 5  | 4
# 25 = 5 * 5

# prime_number = i * something

# i squared = prime_number/i

import time
import math


def check_prime_number(prime_number):
    start_time = time.time()
    message = ' is a prime number'

    if prime_number < 2:
        message = ' is NOT a prime number'
    else:
        for i in range(2, round(math.sqrt(prime_number))):
            if prime_number % i == 0:
                print(str(i) + ' is a divisor')
                message = ' is NOT a prime number'

    print(str(prime_number) + message)
    end_time = time.time()
    print('It took : ' + str(end_time - start_time) + ' seconds')


check_prime_number(45)


