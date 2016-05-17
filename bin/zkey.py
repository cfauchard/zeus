#!/usr/bin/env python3
# coding: utf8
#-----------------------------------------------------------------
# zeus: zkey.py
#
# manipulate zeus secret keys
#
# Copyright (C) 2016, Christophe Fauchard
#-----------------------------------------------------------------

import sys
sys.path.insert(0, "../")

version='1.0.a01'
import argparse
import zeus


parser = argparse.ArgumentParser(description='manipulate zeus secret keys')
parser.add_argument("command", choices=['create'], help="command")
parser.add_argument("--version", action='version', version='%(prog)s ' + version)
parser.add_argument('outfile', type=argparse.FileType('wb'), help="destination key file")                
args = parser.parse_args()

cipher = zeus.Vigenere()
args.outfile.write(cipher.get_key())
