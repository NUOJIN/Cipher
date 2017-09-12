#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 21:08:17 2017

@author: nokicheng
"""

import random,sys,transpositionswap,transpositiondecrypt

def main():
    random.seed(42)
    
    for i in range(20):
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*random.randint(4,40)
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)
        print("Test No {0}: '{1}...'".format(i+1,message[:50]))
        
        for key in range(1,len(message)):
            encrypted = transpositionswap.swap_cipher(message,key)
            decrypted = transpositiondecrypt.swap_decrypt(encrypted,key)
            
            if message != decrypted:
                print('Mismatch with key {0} and message {1}.'.format(key,message))
                print(decrypted)
                sys.exit()
                
    print('Transposition cipher test passed.')
    
if __name__ == '__main__':
    main()