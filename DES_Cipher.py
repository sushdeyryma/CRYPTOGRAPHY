# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 06:12:14 2021

@author: SUSMITA
"""

'''
Write a python program using the built-in Cipher class that encrypts a file 
containing plaintext and decrypts a file containing ciphertext using Triple DES cipher. 
At first, it produces a file (plaintext.txt) 
containing the ciphertext (crypto.txt) and then, 
convert the ciphertext file into plaintext (cleartext.txt).
'''
# Python 3 code to demonstrate
# DES3 algorithms.


from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes


while True:
    try:
        key = DES3.adjust_key_parity(get_random_bytes(24))
        break
    except ValueError:
        pass
    
#open and read the file:
with open('plaintext.txt') as f:
    plaintext = f.read()
    
    

#Encryption
#define encryption variable
def encrypt(msg):
    cipher = DES3.new(key, DES3.MODE_EAX)
    nonce = cipher.nonce
    ciphertext = cipher.encrypt(msg.encode('ascii'))
    return nonce, ciphertext

nonce, ciphertext = encrypt(plaintext)

#generate crypto.txt(containing the ciphertext)
with open("crypto.txt", "wb") as file:
	file.write(ciphertext)
	file.close()
    
#Decryption 
#define decryption variable
def decrypt(nonce, ciphertext):
    cipher = DES3.new(key, DES3.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode('ascii')
         
cleartext = decrypt(nonce, ciphertext)

#generate cleartext.txt(containing the cleartext)
f = open("cleartext.txt", "a")
f.write(cleartext)
f.close()

#print 
print(plaintext) #print the plaintext
print(f'{ciphertext}') #print the ciphertext after encryption
print(f'{cleartext}') #print the cleartext after decryption
