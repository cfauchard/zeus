#!/usr/bin/env python3
# coding: utf8
#-----------------------------------------------------------------
# zeus: crypto.py
#
# provide cryptograhic functions
#
# Copyright (C) 2016, Christophe Fauchard
#-----------------------------------------------------------------

import os
import base64

class Vigenere():

    """
    Vigenere cipher
    
    can handle binary datas for both key and datas
    crypt datas are base64 coded for portability
     
    Parameters:
    - key: key (utf8 string) or filename containing the key
    (if the key is stored in a file, it can contain any binary datas)      
    """
    def __init__(self, key):
    
        if os.path.exists(key):
            f = open(key, 'rb')
            self.key = f.read()
            f.close()
        else:
            self.key = bytearray(key.encode('utf8'))
            
    """
    Parameters:
    - decrypted_datas: decrypted message (utf8 string) or filename containing datas
    (if datas are stored in a file, it can contain any binary datas)
    
    Optionnal parameters:
    - output_filename: file to write encrypted output base64 encoded
    """
    def encrypt(self, decrypted_datas, output_file=None):
        
        if os.path.exists(decrypted_datas):
            f = open(decrypted_datas, 'rb')
            self.decrypted_datas = f.read()
            f.close()
        else:
        	self.decrypted_datas = bytearray(decrypted_datas.encode("utf8"))
        
        self.crypted_datas = bytearray(self.decrypted_datas)               
        j = 0
        for i in range(0, len(self.decrypted_datas)):
            if j == len(self.key):
                j = 0
            self.crypted_datas[i] = (self.decrypted_datas[i] + self.key[j]) % 256
            j += 1
        
        self.crypted_datas = base64.b64encode(self.crypted_datas)
            
        if output_file != None:
        	f = open(output_file, 'wb')
        	f.write(self.crypted_datas)
        	f.close()
         
    """
    Parameters:
    - encrypted_datas: encrypted message (base64 encoded ascii string) or 
    filename containing datas
    
    Optionnal parameters:
    - output_filename: file to write decrypted output
    """
    def decrypt(self, crypted_datas, output_file=None):
        if os.path.exists(crypted_datas):
            f=open(crypted_datas, 'rb')
            self.crypted_datas = bytearray(base64.b64decode(f.read()))
            f.close()
        else:
        	self.crypted_datas = bytearray(base64.b64decode(crypted_datas.encode("utf8")))
        
        self.decrypted_datas = bytearray(self.crypted_datas)    
        j = 0
        for i in range(0, len(self.crypted_datas)):
            if j == len(self.key):
                j = 0
            self.decrypted_datas[i] = (self.crypted_datas[i] - self.key[j]) % 256
            j += 1
        
        self.crypted_datas = base64.b64encode(self.crypted_datas)
        
        if output_file != None:
        	f = open(output_file, 'wb')
        	f.write(self.decrypted_datas)
        	f.close()
        	
    """
    print encrypted datas base64 coded
    """                
    def __str__(self):
        if hasattr(self, 'crypted_datas'):
            return((self.crypted_datas).decode("ascii"))
        else:
            return("No crypted datas in buffer...")
        
if __name__ == '__main__':
    import sys
    sys.path.insert(0, "../")
    import zeus

    print("version zeus: " + zeus.__version__)
    print("Running tests for cryto.py...")

    print("testing class SimpleCrypt...")
    cipher = Vigenere("/bin/ls")
    print(cipher)    
    cipher.encrypt("Itnovem2015", output_file="../sample/crypted.dat")
    print(cipher)
    cipher.decrypt("GG5bbX1lbTMzMTU=", output_file="../sample/decrypted.dat")
    print(cipher)
    print("Class SimpleCrypt passed")

        
     