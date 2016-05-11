#-----------------------------------------------------------------
# zeus: exception.py
#
# Define zeus exception handler
#
# Copyright (C) 2016, Christophe Fauchard
#-----------------------------------------------------------------

import sys
sys.path.insert(0, "../")
import zeus

class FileNotFoundException(Exception):

    def __init__(self, filename):
        self.filename = filename

class InvalidConfigurationFileException(Exception):

    def __init__(self, filename):
        self.filename = filename

