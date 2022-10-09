import platform
import sys
import os
import numpy as np

def encryption(lower, upper, string, seed):
    upper = "".join(upper)
    lower = "".join(lower) 
        
    c_index = 0
    for c in string:
        if c.isalpha():
            if c.isupper():
                string[c_index] = upper[(upper.find(c) + seed) % 26]
            else:
                string[c_index] = lower[(lower.find(c) + seed) % 26]
        else:
            string[c_index] = str(ord(c))
        c_index = c_index + 1
    return "".join(string)

def decryption(lower, upper, string, seed):
    upper = "".join(upper)
    lower = "".join(lower)
    c_index = 0
    for c in string:
        if c.isalpha():
            if c.isupper():
                string[c_index] = upper[(upper.find(c) - seed) % 26]
            else:
                string[c_index] = lower[(lower.find(c) - seed) % 26]
        else:
            string[c_index] = chr(int(c))
                
        c_index = c_index + 1
        
    return "".join(string)    


lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Do you want to encrypt or decrypt or find the shift? [E or D]:')
function = input()

if function == 'E':
    print('Enter your decrypted string:')
    string = input()
    string = list(string)
        
    print('\nEnter your secret seed:')
    seed = int(input())
    
    #Initial string
    print('The initial string is:')
    print("".join(string))
    
    import random
    random.seed(seed)
    
    new_lower = list(lower)
    new_upper = list(upper)
    random.shuffle(new_lower)
    random.shuffle(new_upper)
    
    #Encrypted string
    print('The encrypted string is:')
    print(encryption(new_lower, new_upper, string, seed))
    
elif function == 'D':
    print('Enter your encrypted string:')
    string = input()
    string = list(string)

    #Merge adjacent number in the string in order to be able to
    #find the char associated to che ASCII code
    index = 1
    while index < len(string):
        if string[index].isdigit() and string[index - 1].isdigit():
            string[index - 1] += string.pop(index)
        else:
            index += 1
    
    #print(string_in)
    print('\nEnter your secret seed:')
    seed = int(input())
    
    #Initial string
    print('The initial string is:')
    print("".join(string))
    
    import random
    random.seed(seed)
    
    new_lower = list(lower)
    new_upper = list(upper)
    random.shuffle(new_lower)
    random.shuffle(new_upper)
    
    #Encrypted string
    print('The decrypted string is:')
    print(decryption(new_lower, new_upper, string, seed))
    
    

