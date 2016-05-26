#-----------------------------------------------------------------
# zeus: file.py
#
# Define zeus file tools
#
# Copyright (C) 2016, Christophe Fauchard
#-----------------------------------------------------------------

import os

class Path():

    """
    manipulate paths
    - recursive path create
    - archive path with date create
    """

    def __init__(self, path):
        self.path = path
        self.create(path)

    def create(self, path):
        if os.path.exists(path) or path == "":
            return(True)
        else:
            if not (os.path.exists(os.path.dirname(path))):
                self.create(os.path.dirname(path))
            os.mkdir(path)


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
        self.number = number
        self.size = size

        self.fd = open(self.file_name, "a")

    def print(self, text):
        print(text, file=self.fd)

    def close(self):
        self.fd.close()
