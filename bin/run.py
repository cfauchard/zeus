#!/usr/bin/env python3
# coding: utf8
#-----------------------------------------------------------------
# zeus: run.py
#
# process launcher
#
# Copyright (C) 2016, Christophe Fauchard
#-----------------------------------------------------------------

import os
import sys
import argparse
import zeus

#
# Parse command line arguments
# The option formatter_class=argparse.RawTextHelpFormatter allow
# help fields to be multi lines 
#
args_parser = argparse.ArgumentParser(description = "Process launcher with python environment", 
formatter_class=argparse.RawTextHelpFormatter)
args_parser.add_argument("alias", help = "alias to execute")
args_parser.add_argument("--config_file", default = "run.ini", help = """
Configuration file syntax:
- ini formatted config file
- default config file ./run.ini
- section [alias]
- lines name = <path to a program>

""")
args_parser.add_argument("--list_alias", action="store_false", help = "list aliases configured")
args_parser.add_argument("--version", action = 'version', version = '%(prog)s ' + zeus.__version__)
args_parser.add_argument("arguments", nargs = '*', help = "parameters of the script")
args = args_parser.parse_args()

#
# try to open config file (default run.ini in the working directory)
#
ini_parser = zeus.parser.ConfigParser(args.config_file)

if ini_parser.has_option("alias", args.alias):
    command = ini_parser.get("alias", args.alias)
else:
    print("ERROR: invalid alias " + args.alias)
    sys.exit(0)

separator = " "
command_line = '"' + command + '"' + separator + separator.join(args.arguments)
os.system(command_line)
