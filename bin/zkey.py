#!/usr/bin/env python3
# coding: utf8
#-----------------------------------------------------------------
# zeus: zkey.py
#
# manipulate zeus secret keys
#
# Copyright (C) 2016, Christophe Fauchard
#-----------------------------------------------------------------

import argparse
import zeus

parser = argparse.ArgumentParser(description='manipulate zeus secret keys')
parser.add_argument("command", choices=['create'], help="command")
parser.add_argument("--version", action='version', version='%(prog)s ' + zeus.__version__)
parser.add_argument('outfile', type=argparse.FileType('wb'), help="destination key file")                
args = parser.parse_args()

cipher = zeus.Vigenere()
args.outfile.write(cipher.get_key())
