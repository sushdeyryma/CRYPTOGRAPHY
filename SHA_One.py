# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 23:48:23 2021

@author: SUSMITA
"""

#Write a Python/Java program that implements standard SHA-1 hash function. It takes a file and produces hash value in ‘hvalue.txt’. 
# Python 3 code to demonstrate
# SHA1 hash algorithms.

import hashlib

#open and read the file:
f = open("plaintext.txt", "r")
print(f.read())
str = f.read()

# encoding str using encode()
# then sending to SHA1()
result = hashlib.sha1(str.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())

#produces hash value in ‘hvalue.txt’:
f = open("hvalue.txt", "a")
f.write(result.hexdigest())
f.close()


