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

class SimpleCrypt():

    def __init__(self, key):
        self.key = key
        self.decoded_text = ''
        self.encoded_text = ''
    
    def encrypt(self, decoded_text):
       print(decoded_text[0])
    
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
    cypher = SimpleCrypt("key".encode("utf8"))
    cypher.encrypt("message secret".encode("utf8"))
    print(cypher)
    print("Class SimpleCrypt passed")

        
     
