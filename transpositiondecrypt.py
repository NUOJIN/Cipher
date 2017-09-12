#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 21:22:56 2017

@author: nokicheng
"""
import math
import pyperclip

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
    result = swap_decrypt(message,key)
    print(result,'|')
    pyperclip.copy(result)
    
if __name__ == '__main__':
    main()