#!/usr/bin/env python

import sys
import math

def factorize(number):
    factors = []
    # Check divisibility by 2
    while number % 2 == 0:
        factors.append(2)
        number //= 2

    # Check divisibility by odd numbers starting from 3
    divisor = 3
    while divisor <= math.isqrt(number):
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 2

    if number > 2:
        factors.append(number)

    return factors

def process_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            number = int(line.strip())
            factors = factorize(number)
            print(f'{number}={"*".join(map(str, factors))}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: factors <file>')
        sys.exit(1)

    file_path = sys.argv[1]
    process_file(file_path)
