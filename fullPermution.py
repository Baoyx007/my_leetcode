# -*- coding: utf-8 -*-
__author__ = 'PCPC'


def permution(prefix, str):
    if len(str) <= 0:
        print(prefix)
    else:
        for i in range(len(str)):
            permution(prefix + str[i],str[0:i] + str[i + 1:] )


def combination(str):
    pass


permution('', '12345')
