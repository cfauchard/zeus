#-----------------------------------------------------------------
# zeus: parser.py
#
# Define standard config file parser
#
# Copyright (C) 2016, Christophe Fauchard
#-----------------------------------------------------------------

import os
from configparser import RawConfigParser, MissingSectionHeaderError

class ConfigParser(RawConfigParser):
    def __init__(self, file_name):
        RawConfigParser.__init__(self)
        self.file_name = file_name

        if not os.path.isfile(file_name):
            raise(FileNotFoundException(self.file_name))

        try:
            self.read(self.file_name)

        except MissingSectionHeaderError:
            raise(InvalidConfigurationFileException(self.file_name))

    def __str__(self):
        return_string = ""
        for section in self.sections():
            return_string = return_string + "\n[" + section + "]\n"
            for key in self.items(section):
                return_string = return_string + key[0] + " = " + key[1] + "\n" 
        return(return_string)

        
if __name__ == '__main__':
    import sys
    sys.path.insert(0, "../")
    import zeus

    print("version zeus: " + zeus.__version__)
    print("Running tests for parser.py...")

    print("testing class ConfigParser...")

    try:
        config_file = 'parser_sample1.cfg'
        parser = ConfigParser(config_file)

        print("parsing of " + config_file + " done")
        print(parser)
        print("Class ConfigParser passed")

    except FileNotFoundException as error:
        print("Class ConfigParser not passed, File not found: " + error.filename)
    except:
        print("Class ConfigParser not passed, Unexpected error:", sys.exc_info()[0])
