#!/bin/python3

import math
import os
import random
import re
import sys


def conv_int(m:str) -> int:
    return 0 if m == "" else int(m)


def add(m: str, n: str) -> str:
    dim = max(len(m), len(n))
    if dim < 10:
        return str(conv_int(m) + conv_int(n))

    m = m.zfill(dim)
    n = n.zfill(dim)
    result = [0]*int(dim+1)
    for digit, (i, j) in enumerate(zip(m[::-1], n[::-1])):
        if result[digit] + int(i) + int(j) < 10:
            result[digit] += int(i)+int(j)
        else:
            result[digit+1] = int((result[digit]+int(i)+int(j)) / 10)
            result[digit] = (result[digit]+int(i)+int(j)) % 10
    return "".join(map(str, result))[::-1].lstrip("0")


def __add(l: list) -> str:
    if len(l) == 0:
        return "0"
    last = l.pop(0)  # the biggest num in l
    return add(last, __add(l))


def multiply(m: str, n: str) -> str:
    if len(m) < 4 and len(n) < 4:
        return str(int(m) * int(n))
    result = [[0 for j in range(len(n)+1)] for i in range(len(m)+1)]
    for __i, __char_m in enumerate(m):
        for __j, __char_n in enumerate(n):
            # multiply one digit by one digit
            result[__i][__j] = int(__char_m) * int(__char_n)

    dim = len(m)+len(n) # dim - 1 equals the num of sum. len(range(dim)) = dim
    rl_diag = [""]*(dim-1)
    for k in range(1, dim): # m,n=2,3 dim=5, range(1,dim)=[1,2,3,4]
        diag_total = 0
        for i in range(len(m)):
            try:
                diag_total += result[i][k-i-1] # k=1, range(k)=[0], k=2, range(k)=[0,1]
            except Exception as e:
                raise Exception(diag_total, e, k, i, m, n, dim, result)
        rl_diag[k-1] = str(diag_total) + "0" * (dim-1-k)
    return __add(rl_diag)


# Complete the extraLongFactorials function below.
def extraLongFactorials(n: str) -> str:
    if n == "1":
        return "1"
    return multiply(str(n), extraLongFactorials(str(int(n)-1)))


if __name__ == '__main__':
    n = int(input())

    print(extraLongFactorials(n))
