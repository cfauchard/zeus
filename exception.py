#-----------------------------------------------------------------
# zeus: exception.py
#
# Define zeus exception handler
#
# Copyright (C) 2016, Christophe Fauchard
#-----------------------------------------------------------------

class FileNotFoundException(Exception):

    def __init__(self, filename):
        self.filename = filename

class InvalidConfigurationFileException(Exception):

    def __init__(self, filename):
        self.filename = filename
