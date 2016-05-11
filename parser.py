#-----------------------------------------------------------------
# zeus: parser.py
#
# Define standard config file parser
#
# Copyright (C) 2016, Christophe Fauchard
#-----------------------------------------------------------------

import sys
sys.path.insert(0, "../")
import zeus

import os
import itertools
from zeus.exception import FileNotFoundException, InvalidConfigurationFileException
from configparser import RawConfigParser


class ConfigParser(RawConfigParser):
    def __init__(self, file_name):
        RawConfigParser.__init__(self)
        self.file_name = file_name

        if not os.path.isfile(file_name):
            raise(zeus.exception.FileNotFoundException(self.file_name))

        try:
            self.read(self.file_name)

        except configparser.MissingSectionHeaderError:
            raise(zeus.exception.InvalidConfigurationFileException(self.file_name))

if __name__ == '__main__':
    
    print("version zeus: " + zeus.__version__)
    print("Running tests for parser.py...")

    print("testing class ConfigParser...")

    try:
        config_file = 'parser_sample1.cfg'
        parser = zeus.ConfigParser(config_file)

        print("parsing of " + config_file + " done");
        for section in parser.sections():
            print(section)
            for key in parser.items(section):
                print(key)

        print("Class ConfigParser passed")

    except zeus.exception.FileNotFoundException as error:
        print("Class ConfigParser not passed, File not found: " + error.filename)
    except:
        print("Class ConfigParser not passed, Unexpected error:", sys.exc_info()[0])
