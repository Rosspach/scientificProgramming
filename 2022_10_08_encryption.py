import platform
import sys
import os
import numpy as np

def encryption(lower, upper, string, shift):
    c_index = 0
    for c in string:
        if c.isalpha():
            if c.isupper():
                string[c_index] = upper[(upper.find(c) + shift) % 26]
            else:
                string[c_index] = lower[(lower.find(c) + shift) % 26]
        c_index = c_index + 1
        
    return "".join(string)

def decryption(lower, upper, string, shift):
    c_index = 0
    for c in string:
        if c.isalpha():
            if c.isalpha():
                if c.isupper():
                    string[c_index] = upper[(upper.find(c) - shift) % 26]
                else:
                    string[c_index] = lower[(lower.find(c) - shift) % 26]
            
        c_index = c_index + 1
        
    return "".join(string)

def find_shift(lower, upper, string, shift):
    c_index = 0
    for c in string:
        if c.isalpha():
            if c.isalpha():
                if c.isupper():
                    string[c_index] = upper[(upper.find(c) - shift) % 26]
                else:
                    string[c_index] = lower[(lower.find(c) - shift) % 26]
            
        c_index = c_index + 1
        
    return "".join(string)
    

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Do you want to encrypt or decrypt or find the shift? [E or D or F]:')
function = input()

if function == 'E':
    print('Enter your decrypted string:')
    string = input()
    string = list(string)
    print('\nEnter your shift:')
    shift = int(input())
    
    #Initial string
    print('The initial string is:')
    print("".join(string))
    
    #Encrypted string
    print('The encrypted string is:')
    print(encryption(lower, upper, string, shift))
    
elif function == 'D':
    print('Enter your encrypted string:')
    string = input()
    string = list(string)
    
    print('\nEnter your shift:')
    shift = int(input())
    
    #Initial string
    print('The initial string is:')
    print("".join(string))
    
    #Encrypted string
    print('The decrypted string is:')
    print(decryption(lower, upper, string, shift))
    
elif function == 'F':
    print('Enter your encrypted string:')
    string = input()
    string = list(string)
    
    #Initial string
    print('The initial string is:')
    print("".join(string))
    
    for i in np.arange(0,26,1): #brutal force
        print(decryption(lower, upper, string, i))
        print('The decrypted string is with shift {}:'.format(i))

    
            

