#!/usr/bin/env python3
# coding: utf8
#-----------------------------------------------------------------
# zeus: parser.py
#
# Define standard config file parser
#
# Copyright (C) 2016, Christophe Fauchard
#-----------------------------------------------------------------

import os
from configparser import RawConfigParser, MissingSectionHeaderError
import zeus
import xml.etree.ElementTree

class XmlParser():
 	def __init__(self, file_name):
 		self.file_name = file_name
 		
 		self.tree = xml.etree.ElementTree.parse(self.file_name)

class ConfigParser(RawConfigParser):
    def __init__(self, file_name):
        RawConfigParser.__init__(self)
        self.file_name = file_name

        if not os.path.isfile(file_name):
            raise(zeus.exception.FileNotFoundException(self.file_name))

        try:
            self.read(self.file_name)

        except MissingSectionHeaderError:
            raise(zeus.exception.InvalidConfigurationFileException(self.file_name))

    def __str__(self):
        return_string = ""
        for section in self.sections():
            return_string = return_string + "\n[" + section + "]\n"
            for key in self.items(section):
                return_string = return_string + key[0] + " = " + key[1] + "\n" 
        return(return_string)
