#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 18:11:50 2017

@author: nokicheng
"""

import sys,pyperclip,cryptomath,random
#SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ^_`abcdefghijklmnopqrstuvwxyz{|}~"""
SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def main():
    #myMessage = """"A computer would deserve to be called intelligent if it could deceive a human into beliecing that it was human." -Alan Turing"""
    myMessage = """IP~W?tTdL%"~/?d_o~o%7%"y%~L?~B%~W-__%o~|*L%__|O%*L~|:~|L~W?d_o~o%W%|y%~-~gdt-*~|*L?~B%_|%W|*O~Lg-L~|L~/-7~gdt-*1I~{P_-*~rd"|*O"""
    myKey = 2023
    myMode = 'decrypt'
    #myMode = 'encrypt'
    
    if myMode == 'encrypt':
        translated = encryptMessage(myKey,myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey,myMessage)
    print('Key:',myKey)
    print('{0}ed text:'.format(myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print('Full {0}ed text copied to clipboard.'.format(myMode))
    
def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA,keyB)

def checkKeys(keyA,keyB,mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit('The affine cipher becomes incredibly weak when key A is set to 1. Choose a different key.')
    if keyB == 0 and mode == 'encrypt':
        sys.exit('The affine cipher becomes incredibly weak when key B is set to 0. Choose a different key.')
    if keyA < 0 or keyB < 0 or keyB >len(SYMBOLS)-1:
        sys.exit('Key A must be greater than 0 and Key B must be between 0 and {0}.'.format(len(SYMBOLS)-1))
    if cryptomath.gcd(keyA,len(SYMBOLS)) != 1:
        sys.exit('Key A ({0}) and the symbol set size ({1}) are not relatively prime. Choose a different key.'.format(keyA,len(SYMBOLS)))

def encryptMessage(key,message):
    keyA,keyB = getKeyParts(key)
    checkKeys(keyA,keyB,'encrypt')
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symIndex*keyA+keyB)%len(SYMBOLS)]
        else:
            ciphertext += symbol
    return ciphertext

def decryptMessage(key,message):
    keyA,keyB = getKeyParts(key)
    checkKeys(keyA,keyB,'decrypt')
    plaintext = ''
    modInverseOfKeyA = cryptomath.findModInverse(keyA,len(SYMBOLS))
    
    for symbol in message:
        if symbol in SYMBOLS:
            symIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            plaintext += symbol
    return plaintext
    
def getRandomKey():
    while True:
        keyA = random.randint(2,len(SYMBOLS))
        keyB = random.randint(2,len(SYMBOLS))
        if cryptomath.gcd(keyA,len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB
        
if __name__ == '__main__':
    main()