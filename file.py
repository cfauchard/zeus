#-----------------------------------------------------------------
# zeus: file.py
#
# Define hermes config file parser
#
# Copyright (C) 2016, Christophe Fauchard
#-----------------------------------------------------------------

class Log():
    """
    Log Class with switch capabilities
    """
    
    def __init__(self, \
                 file_name, \
                 number=10, \
                 size=1, \
                 frequence=None, \
                 ):
        
        self.file_name = file_name
        self.frequence = frequence
        number = number
        size = size

                
