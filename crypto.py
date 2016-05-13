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

class SimpleCrypt():

    def __init__(self, key):
        self.key = key
        self.byte_key = bytearray(self.key.encode("latin1"))
    
    def encrypt(self, decoded_text):
        self.decoded_text = decoded_text
        self.byte_decoded_text = bytearray(self.decoded_text.encode("latin1"))
        self.byte_encoded_text = bytearray(self.decoded_text.encode("latin1"))        
                
        j = 0
        for i in range(0, len(self.byte_decoded_text)):
            if j == len(self.byte_key):
                j = 0
            self.byte_encoded_text[i] = self.byte_decoded_text[i] + self.byte_key[j]
            j += 1
        
        self.encoded_text = self.byte_encoded_text.decode("latin1")
 
    def decrypt(self, encoded_text):
        self.encoded_text = encoded_text
        self.byte_decoded_text = bytearray(self.encoded_text.encode("latin1"))
        self.byte_encoded_text = bytearray(self.encoded_text.encode("latin1"))
                
        j = 0
        for i in range(0, len(self.byte_encoded_text)):
            if j == len(self.byte_key):
                j = 0
            self.byte_decoded_text[i] = self.byte_encoded_text[i] - self.byte_key[j]
            j += 1
        
        self.decoded_text = self.byte_decoded_text.decode("latin1")
            
    def __str__(self):
        return_string = "decoded text: " + self.decoded_text + "\nencoded text: " + self.encoded_text
        return(return_string)
        
if __name__ == '__main__':
    import sys
    sys.path.insert(0, "../")
    import zeus

    print("version zeus: " + zeus.__version__)
    print("Running tests for cryto.py...")

    print("testing class SimpleCrypt...")
    cypher = SimpleCrypt("fghnfvcghklmbd45689JGHB")
    cypher.encrypt("message secret")
    print(cypher)
    cypher.decrypt(cypher.encoded_text)
    print(cypher)
    print("Class SimpleCrypt passed")

        
     
