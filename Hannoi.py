#!/usr/bin/python

def Hannoi(n, a, b, c):
    if n == 1:
        print a, '-->', c
        return
    else:
        Hannoi(n-1, a, c, b)
        print a, '-->', c
        Hannoi(n-1, b, a, c)
        return

Hannoi(4, 'A', 'B', 'C')


