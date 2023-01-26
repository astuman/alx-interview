#!/usr/bin/python3
# pascal_triangle.py
def pascal_triangle(n):
    if n <= 0:
        return [{}]
    for i in range(n, n+1):
        for j in range(0, n-i+1):
            print('', end='')
            c = 1
        for j in range(1, i+1):
            print('', c, sep='', end='')
            cc = c * (i-j) // j
            print()
