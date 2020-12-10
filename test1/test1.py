'''
author: skottZy
date: 2020/11/23
sumarry: test1.py
'''

import time

n = int(1e8)

def sum1(n: int) -> int:

    sum = 0
    for x in range(n):
        sum += pow(-1, x)

    return sum


def sum2(n: int) -> int:

    sum = 0
    if n % 2 == 0:
        sum = 0

    else:
        sum = -1
    return sum


if __name__ == '__main__':

    print("starting...")

    # sum1
    startTime = time.process_time()
    res1 = sum1(n)
    print(f"sum: {res1}")
    endTime = time.process_time()
    print(f"time: {endTime - startTime:.2f}s")

    #sum2
    startTime = time.process_time()
    res2 = sum2(n)
    print(f"sum: {res1}")
    endTime = time.process_time()
    print(f"time: {endTime - startTime:.2f}s")

