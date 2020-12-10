'''
author: skottZy
date: 2020/12/10
sumarry: test2.py
'''

def fac(n: int) -> int:

    if (n < 0):
        print("n < 0, data error!")
        return -1
    elif n == 0 or n == 1:
        return 1

    else:
        return n * fac(n - 1)


if __name__ == '__main__':
    n = fac(5)
    print(n)