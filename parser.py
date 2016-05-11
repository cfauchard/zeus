#-----------------------------------------------------------------
# zeus: parser.py
#
# Define hermes config file parser
#
# Copyright (C) 2016, Christophe Fauchard
#-----------------------------------------------------------------

import itertools
from zeus.exception import FileNotFoundException, InvalidConfigurationFileException
from configparser import RawConfigParser


class ConfigParser(RawConfigParser):
    def __init__(self, file_name):
        RawConfigParser.__init__(self)
        self.file_name = file_name

        try:
            self.read(self.file_name)

        except configparser.MissingSectionHeaderError:
            raise(InvalidConfigurationFileException(self.file_name))

            
                
