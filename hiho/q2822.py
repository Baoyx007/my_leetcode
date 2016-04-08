# -*- coding: utf-8 -*-
__author__ = 'PCPC'


def reverse(s):
    mid = len(s) // 2
    length = len(s)
    while mid > 1:
        if s[mid - 1] != s[length-mid]:
            return False
        mid -= 1
    return True

print(reverse('dsfd'))
