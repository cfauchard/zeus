#!/usr/bin/env python3
# coding: utf8
#-----------------------------------------------------------------
# zeus: zcrypt.py
#
# encrypt/decrypt files using zeus.Vigenere class
#
# Copyright (C) 2016, Christophe Fauchard
#-----------------------------------------------------------------

version='1.0.a01'
import argparse
import sys
import pypath
import zeus

parser = argparse.ArgumentParser(description='encrypt/decrypt files using zeus.Vigenere class')
parser.add_argument("command", choices=['crypt','decrypt'], help="command")
parser.add_argument('keyfile', help="key file name")
parser.add_argument("--version", action='version', version='%(prog)s ' + version)
parser.add_argument('--infile', help="source data file (can be every binary file)")
parser.add_argument('--outfile', help="destination data file (can be every binary file)")
parser.add_argument('--string', help="string to encrypt (must be an utf8string)")                
args = parser.parse_args()

cipher = zeus.Vigenere(args.keyfile)

if args.command == 'crypt':
	if args.string != None:
		cipher.encrypt(args.string, output_file=args.outfile)
	elif args.infile != None:
		cipher.encrypt(args.infile, output_file=args.outfile)
		
	if args.outfile == None:
		print(cipher.get_crypted_datas().decode("ascii"))
	
elif args.command == 'decrypt':
	if args.string != None:
		cipher.decrypt(args.string, output_file=args.outfile)
	elif args.infile != None:
		cipher.decrypt(args.infile, output_file=args.outfile)

	
	if args.outfile == None:
		print(cipher.get_decrypted_datas().decode("utf8"))

		
