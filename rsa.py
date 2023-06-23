#!/usr/bin/env python

import sys
import math

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, math.isqrt(number) + 1):
        if number % i == 0:
            return False
    return True

def factorize(number):
    factors = []
    # Check divisibility by 2
    while number % 2 == 0:
        factors.append(2)
        number //= 2

    # Check divisibility by odd primes starting from 3
    divisor = 3
    while divisor <= math.isqrt(number):
        if number % divisor == 0 and is_prime(divisor):
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 2

    if number > 2:
        factors.append(number)

    return factors

def process_file(file_path):
    with open(file_path, 'r') as file:
        number = int(file.readline().strip())
        factors = factorize(number)
        print(f'{number}={"*".join(map(str, factors))}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: rsa <file>')
        sys.exit(1)

    file_path = sys.argv[1]
    process_file(file_path)
