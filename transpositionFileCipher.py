#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:37:12 2017

@author: nokicheng
"""

import time,os,sys,transpositionswap,transpositiondecrypt

def main():
    inputFilename = 'Frankenstein_decrypt.txt'
    outputFilename = 'Frankenstein_encrypt.txt'
    myKey = 10
    myMode = 'decrypt'
    
    if not os.path.exists(inputFilename):
        print('The file {0} does not exist. Quitting...'.format(inputFilename))
        sys.exit()
        
    if os.path.exists(outputFilename):
        print('This will overwrite the file {0}. (C)ontinue or (Q)uit?'.format(outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()
            
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()
    
    print('{0}ing...'.format(myMode.title()))
    
    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionswap.swap_cipher(content,myKey)
    elif myMode == 'decrypt':
        translated = transpositiondecrypt.swap_decrypt(content,myKey)
    totalTime = round(time.time()-startTime,2)
    print('{0}ion time: {1} seconds'.format(myMode.title(),totalTime))
    
    outputFileObj = open(outputFilename,'w')
    outputFileObj.write(translated)
    outputFileObj.close()
    
    print('Done {0}ing {1} ({2} characters)'.format(myMode,inputFilename,len(content)))
    print('{0}ed file is {1}.'.format(myMode.title(),outputFilename))
    
if __name__ == '__main__':
    main()