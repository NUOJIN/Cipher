#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 21:51:57 2017

@author: nokicheng
"""

import pyperclip,sys,random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    #myMessage = 'If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained in this way. -Bertrand Russell'
    myMessage = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm'
    myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    myMode = 'decrypt'
    
    checkValidKey(myKey)
    
    if myMode == 'encrypt':
        translated = encryptMessage(myKey,myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey,myMessage)
    
    print('Using key {0}'.format(myKey))
    print('The {0}ed message is:'.format(myMode))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('This message has been copied to the clipboard.')
    

def checkValidKey(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        sys.exit('There is an error in the key or symbol set.')
        

def encryptMessage(key,message):
    return translateMessage(key,message,'encrypt')

def decryptMessage(key,message):
    return translateMessage(key,message,'decrypt')


def translateMessage(key,message,mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        charsA,charsB = charsB,charsA
    
    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol
            
    return translated

def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)

if __name__ == '__main__':
    main()