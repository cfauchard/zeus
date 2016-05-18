#!/usr/bin/env python3
# coding: utf8
#-----------------------------------------------------------------
# zeus: run.py
#
# set environment and launch python scripts
#
# Copyright (C) 2016, Christophe Fauchard
#-----------------------------------------------------------------

import os
import sys
import argparse

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("PYTHONPATH", base_dir)
sys.path.insert(0, base_dir)

import zeus

parser = argparse.ArgumentParser(description='zeus environment setting')
parser.add_argument("command", help="script to execute")
parser.add_argument("arguments", nargs='*', help="parameters of the script")
args = parser.parse_args()

separator = " "
command_line = args.command + separator + separator.join(args.arguments)
os.system(command_line)
