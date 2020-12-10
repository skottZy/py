'''
author: skottZy
date: 2020/12/10
sumarry: test3.py
'''

import time

def fib1(n: int):

    if n < 1:
        return -1

    elif n == 1 or n == 2:
        return 1

    else:
        return fib1(n - 1) + fib1(n - 2)

def fib2(n: int):

    if n < 1:
        return -1
    res = 0

    tmpList = [0] * (n + 1)

    tmpList[1] = tmpList[2] = 1

    for i in range(3, n + 1):
        tmpList[i] = tmpList[i - 1] + tmpList[i - 2]

    res = tmpList[n]

    return res

if __name__ == '__main__':

    startTime = time.process_time()
    n = 35

    res2 = fib2(n)
    print(f"fib({n}) = {res2} time: {time.process_time() - startTime:.2f}s")

    res1 = fib1(n)
    print(f"fib({n}) = {res1} time: {time.process_time() - startTime:.2f}s")