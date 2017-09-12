#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 21:03:14 2017

@author: nokicheng
"""

#Caesar Cipher
import pyperclip
def caesar_cipher(message,key,mode):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translated = ''
    message = message.upper()
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode == 'encrypt':
                num = num + key
            if mode == 'decrypt':
                num = num - key
        
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            if num < 0:
                num = num + len(LETTERS)
            
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
    #pyperclip.copy(translated)
    return translated

def decrypt(message):
    for i in range(26):
        print(caesar_cipher(message,i,'decrypt'))
        
def main():
    message = "Common sense is not so common."
    key = 8
    print(caesar_cipher(message,key,'encrypt'),'|')
    pyperclip.copy(caesar_cipher(message,key,'encrypt'))

if __name__ == '__main__':
    main()