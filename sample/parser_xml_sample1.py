#!/usr/bin/env python3
# coding: utf8
#-----------------------------------------------------------------
# zeus: parser_xml_sample.py
#
# process launcher
#
# Copyright (C) 2016, Christophe Fauchard
#-----------------------------------------------------------------

import argparse
import sys
import zeus

#
# Parse command line arguments
# The option formatter_class=argparse.RawTextHelpFormatter allow
# help fields to be multi lines 
#
args_parser = argparse.ArgumentParser(description = "Sample for parsing XML files", 
formatter_class=argparse.RawTextHelpFormatter)
args_parser.add_argument("--version", action = 'version', version = '%(prog)s ' + zeus.__version__)
args_parser.add_argument("xml_file",  help = "xml file")
args = args_parser.parse_args()

print("version zeus: " + zeus.__version__)
print("Running tests for parser.py...")

print("testing class XmlParser...")

try:
	print("parsing of " + args.xml_file + "...")
	parser = zeus.XmlParser(args.xml_file)

	print("parsing of " + args.xml_file + " done")
	for Country in parser.root:
		print(Country.tag, Country.attrib, flush=True)
		for level2 in Country:
			print(level2.tag, level2.attrib, level2.text, flush=True)
				

except FileNotFoundError as error:
	print("Class XmlParser not passed, File not found: " + error.filename)
else:
	print("Class XmlParser passed")