# coding=utf-8

"""
斐波拉契数列
"""

meno = {0: 0, 1: 1}  # 初始化 最初的两个值


def fib(n):
    if not n in meno:  # 如果不在初始值范围内
        meno[n] = fib(n - 1) + fib(n - 2)
    return meno[n]


if __name__ == "__main__":
    f = fib(10)
    print f
