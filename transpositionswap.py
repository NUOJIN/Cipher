#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 20:52:53 2017

@author: nokicheng
"""

#Swap Cipher
import pyperclip
import math
def swap_cipher(message,key):
    pointer = 0
    text = ['']*key
    for symbol in message:
        text[pointer%key] = text[pointer%key] + symbol
        pointer += 1
    return ''.join(text)
    
def swap_decrypt(message,key):
    column = math.ceil(len(message)/key)
    lack = key*column - len(message)
    text = ['']*column
    col = row = 0
    for symbol in message:
        text[col] += symbol
        col += 1
        if (col == column) or (col==column-1 and row>=key-lack):
            row += 1
            col = 0
    return ''.join(text)

def main():
    message = 'common sense is not so common.'
    key = 8
    result = swap_cipher(message,key)
    print(result,'|')
    result2 = swap_decrypt(result,key)
    print(result2,'|')
    pyperclip.copy(result)
if __name__ == '__main__':
    main()