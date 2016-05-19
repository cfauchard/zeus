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
import pypath
import zeus

args_parser = argparse.ArgumentParser(description='process launcher')
args_parser.add_argument("alias", help="alias to execute")
args_parser.add_argument("--config_file", default="run.ini", help="configuration file")
args_parser.add_argument("--list_alias", action="store_false", help="list aliases configured")
args_parser.add_argument("arguments", nargs='*', help="parameters of the script")
args = args_parser.parse_args()

ini_parser = zeus.parser.ConfigParser(args.config_file)

if ini_parser.has_option("alias", args.alias):
    command = ini_parser.get("alias", args.alias)
else:
    print("ERROR: invalid alias " + args.alias)
    sys.exit(0)

separator = " "
command_line = '"' + command + '"' + separator + separator.join(args.arguments)
os.system(command_line)
