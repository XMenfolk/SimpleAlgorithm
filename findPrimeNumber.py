# coding=utf-8

"""
寻找素数
"""

import math


def is_prime(n):
    """
    判断一个数是否是素数
    :param n:
    :return:
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
        return True

if __name__ == "__main__":
    primes = [i for i in range(2, 100) if is_prime(i)]
    print primes